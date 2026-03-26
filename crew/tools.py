"""
tools.py
--------
Custom CrewAI tool — CVReaderTool reads uploaded CV file
and returns raw text + pre-processed summary to Agent 1.
"""



from typing import Type
from pydantic import BaseModel
from crewai.tools import BaseTool

from utils.cv_parser import extract_cv_text, simple_cv_summary


class CVReadInput(BaseModel):
    file_path: str


class CVReaderTool(BaseTool):
    name: str = "cv_reader_tool"
    description: str = (
        "Use this tool to read a candidate's CV file from disk. "
        "Accepts PDF, DOCX, or TXT file path. "
        "Returns the full raw text and a basic pre-processed summary. "
        "Always use this tool first before analyzing any CV."
    )
    args_schema: Type[BaseModel] = CVReadInput

    def _run(self, file_path: str) -> str:
        try:
            raw_text = extract_cv_text(file_path)

            if not raw_text.strip():
                return "ERROR: CV file is empty or could not be read. Please check the file."

            summary = simple_cv_summary(raw_text)

            return (
                "=== RAW CV TEXT ===\n"
                + summary["raw_text"]
                + "\n\n=== CANDIDATE NAME (first line guess) ===\n"
                + summary["name_guess"]
                + "\n\n=== EXPERIENCE SNIPPET (first 30 lines) ===\n"
                + summary["experience_snippet"]
            )

        except FileNotFoundError:
            return f"ERROR: File not found at path: {file_path}"
        except Exception as e:
            return f"ERROR: Failed to read CV — {str(e)}"
