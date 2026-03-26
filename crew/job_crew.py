from __future__ import annotations

import os
from dotenv import load_dotenv

from crewai import Agent, Task, Crew, Process, LLM
from crewai.project import CrewBase, agent, task, crew

from crew.tools import CVReaderTool

load_dotenv()


@CrewBase
class JobApplicationCrew:
    """Orchestrates CV Analyzer + Job Matcher + Cover Letter Writer agents."""

    agents_config = "config/agents.yaml"
    tasks_config  = "config/tasks.yaml"

    # ---------- LLM ----------
    def _llm(self) -> LLM:
        return LLM(
            model="gpt-4o-mini",
            temperature=0.4,
            timeout=90,
            api_key=os.getenv("OPENAI_API_KEY"),
        )

    # ---------- Agents ----------
    @agent
    def cv_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["cv_analyst"],
            tools=[CVReaderTool()],
            llm=self._llm(),
        )

    @agent
    def job_matcher(self) -> Agent:
        return Agent(
            config=self.agents_config["job_matcher"],
            llm=self._llm(),
        )

    @agent
    def cover_letter_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["cover_letter_writer"],
            llm=self._llm(),
        )

    # ---------- Tasks ----------
    @task
    def cv_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config["cv_analysis_task"],
            agent=self.cv_analyst(),
        )

    @task
    def job_match_task(self) -> Task:
        return Task(
            config=self.tasks_config["job_match_task"],
            agent=self.job_matcher(),
            context=[self.cv_analysis_task()],
        )

    @task
    def cover_letter_task(self) -> Task:
        return Task(
            config=self.tasks_config["cover_letter_task"],
            agent=self.cover_letter_writer(),
            context=[self.cv_analysis_task(), self.job_match_task()],
        )

    # ---------- Crew ----------
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )

    # ---------- Run helper ----------
    def run(self, cv_file_path: str, job_description: str, candidate_name: str) -> dict:
        result = self.crew().kickoff(
            inputs={
                "cv_text": cv_file_path,       # passed to tasks.yaml {cv_text}
                "job_description": job_description,
                "candidate_name": candidate_name,
            }
        )

        # extract each task output cleanly
        outputs = result.tasks_output
        return {
            "cv_summary":    outputs[0].raw if len(outputs) > 0 else "",
            "match_report":  outputs[1].raw if len(outputs) > 1 else "",
            "cover_letter":  outputs[2].raw if len(outputs) > 2 else "",
        }
