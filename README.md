Got it! Here's the `README.md` in the exact same style: [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/75679719/fb66ca20-3ee7-4b11-9a95-db81cc0e1d4c/README.md?AWSAccessKeyId=ASIA2F3EMEYE5EJ3KZQU&Signature=adp3zB8kzNHJ%2BG5wzlRzuDu8o%2Fg%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEAEaCXVzLWVhc3QtMSJHMEUCIQC3KziyFjc2HdU9WsPMWib3UnYDpqOy%2FW47EUk3X%2F9qtwIgLWCg2wO8GuVhuAITXUk0hz5ImtWeNI9BswodAMk84yIq%2FAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDMYQy8%2FyYkPC8l0bZSrQBIgrwWTnHuWrkJ5NwcVQcj0mN4dCakIxPNrhneduim0tjPxi28Lz%2FYB9%2BPb8Y14dePWPYHhS2oCsjIh3Jtw6BDi%2BOHEEHU0NhxRhhOzzoOxpANCrodQrEswdz7IxH7eu3XiMmLyHW3%2FYakVvTTKsA6WRA6Ggpgpw83edtcDSm9htKTJGh0aoymiuY2Bja93HszVR4jiT%2F7KAfp4bpnuxgW1cni%2B4RseKTafDLRBDoPOL7F71mh5qvGRR1R2kBcSmHmCYSKnoOqofZXWhqJ08imfpxD%2B1qRrdxpxXn%2Bh7efL%2FiWbRTkiZBgDh%2BRvmotRSN0N1y9335jnqjQ%2BEsV9yQW%2Ff8TlQSEi24nyxteoCC40mh3kThpq4O%2Bqq9TG%2BenoYHcx7VTffXeBUd1wJ95DkFq4RehnC%2Fqc3UmmkJyw2pRVtvWgIra8%2BwQT2B8d%2Blj8HQcmILC1oOlMug53U62G4eJzq3fD%2F6sZ37HCUp664RRTxLklX%2FOmvQFJBGE%2FgnVQxh2A0n9%2FHWZUFp8f1JCp%2FO0cFnZo%2F6tT4pw7ahzSfGEkRHzijYpltM25rKMP3anGTqV3%2BfWKT%2BUMOdP84YtlEOI7UIqyAVcniaBCA3o1KNtmPLqx40QalkVrJkVwOLZbnxlv1BWq0O19EkLdgGwhg%2BWcTrOdD43sNvHdtPWD0Yp%2F%2FWDRuRSApY7wpgLMt3Lp7sbUuFRetlYKLb5ej8kHzaiDYrvffCcp1lGYc%2BR6kl7Re66W4%2BD%2Bt%2Fk5Vdt3IFsGu9y2PIVRVyM%2FL1XjYyVCmtTcwtbSVzgY6mAEW2gC6d34E2yE8l%2FjFC3JWkuzYBX7FUkTZl5qSsCE2MhxM1QF%2FFu2UUShTApTkkhStm7Y%2F%2Fw8o%2BjigIsrnzttJWrj7dFWq%2BHPVCwdoXBhcTv17VeW2dcwW1SlfyQTneYtuR0B51Z8%2B5fJPfkC0svcexswwNf%2BoAPmHkxVun%2F1Yvq%2Bam4m8cQ7tD53YsNVz84VZHSAMSQLwSw%3D%3D&Expires=1774542244)

***

## `README.md`

```markdown
# 💼 Job Application Crew

> 3-agent CrewAI crew — CV Analyzer + Job Matcher + Cover Letter Writer

![Python](https://img.shields.io/badge/Python-3.11-blue)
![CrewAI](https://img.shields.io/badge/CrewAI-Latest-orange)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red)

---

## 📌 What Is This?

A 3-agent CrewAI crew that automates the job application process. The CV Analyst agent reads and structures your resume. The Job Matcher agent compares it against a job description and scores the fit. The Cover Letter Writer agent produces a tailored, ready-to-send cover letter. Built using CrewAI Agents, Tasks, Crew, YAML config, and sequential process.

---

## 🗺️ Simple Flow
```
User provides CV + Job Description + Name
        ↓
  [CV Analyst Agent]
  Reads CV via CVReaderTool
  Produces structured CV summary
        ↓
  [Job Matcher Agent]
  Compares CV summary with job description
  Produces match report + fit score
        ↓
  [Cover Letter Writer Agent]
  Uses CV summary + match report
  Writes tailored cover letter
        ↓
  All 3 outputs displayed + downloadable
```

---

## 🏗️ Detailed Architecture
```
User
 ├── streamlit_app.py     → Web UI
 └── app.py               → Terminal interface
          │
          ▼
      crew/
      ├── job_crew.py     → Loads YAML + wires agents, tasks, crew
      └── tools.py        → CVReaderTool for CV Analyst
          │
          ▼
      config/
      ├── agents.yaml     → Agent definitions (role, goal, backstory)
      └── tasks.yaml      → Task definitions (description, expected output)
          │
          ▼
      utils/
      └── cv_parser.py    → Extracts text from PDF / DOCX / TXT
          │
          ▼
      CrewAI → sequential process
      OpenAI → gpt-4o-mini
```

---

## 📁 Project Structure
```
job-application-crew/
├── app.py                  ← Terminal version
├── streamlit_app.py        ← Web UI (deploy this)
├── config/
│   ├── agents.yaml         ← Agent role, goal, backstory
│   └── tasks.yaml          ← Task description, expected output
├── crew/
│   ├── __init__.py
│   ├── job_crew.py         ← Crew definition
│   └── tools.py            ← CVReaderTool
├── utils/
│   ├── __init__.py
│   └── cv_parser.py        ← PDF/DOCX/TXT text extractor
├── outputs/                ← Auto-generated result files (CLI)
├── .env                    ← API keys (never push!)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🧠 Key Concepts

| Concept | What It Does |
|---|---|
| **Agent** | Autonomous AI worker with role, goal, backstory |
| **Task** | Work assigned to an agent with description + expected output |
| **Crew** | Orchestrates agents and tasks together |
| **Sequential Process** | Agent 1 finishes → output passed to Agent 2 → Agent 3 |
| **YAML Config** | Agent and task definitions in clean config files |
| **context=[...]** | Each task receives previous task output automatically |
| **CVReaderTool** | Custom tool that reads PDF/DOCX/TXT and passes text to Agent 1 |
| **memory: true** | Agents remember context across tasks |

---

## 🔄 CrewAI vs LangGraph

| Feature | LangGraph | CrewAI |
|---|---|---|
| Control | Full — you define every node and edge | High level — agents decide how to work |
| Complexity | More code | Less code |
| Flexibility | Maximum | Less customizable |
| Best for | Complex workflows needing precise control | Multi-agent collaboration |

---

## ⚙️ Local Setup

**Step 1 — Clone:**
```bash
git clone https://github.com/Venkata1236/job-application-crew.git
cd job-application-crew
```

**Step 2 — Install:**
```bash
pip install -r requirements.txt
```

**Step 3 — Add API key:**

`.env`:
```
OPENAI_API_KEY=your_openai_key
```

`.streamlit/secrets.toml`:
```toml
OPENAI_API_KEY = "your_openai_key"
```

**Step 4 — Run:**
```bash
python -m streamlit run streamlit_app.py
python app.py
```

---

## 🚀 Deploy on Streamlit Cloud

1. Push to GitHub
2. Go to share.streamlit.io
3. Connect repo → select `streamlit_app.py`
4. Settings → Secrets → add `OPENAI_API_KEY`
5. Click Deploy ✅

---

## 📦 Tech Stack

- **CrewAI** — Agents, Tasks, Crew, sequential process
- **crewai-tools** — BaseTool for custom CVReaderTool
- **OpenAI** — GPT-4o-mini
- **Streamlit** — Web UI
- **PyPDF2** — PDF text extraction
- **python-docx** — DOCX text extraction
- **python-dotenv** — API key management

---

## 👤 Author

**Venkata Reddy Bommavaram**
- 📧 bommavaramvenkat2003@gmail.com
- 💼 [LinkedIn](https://linkedin.com/in/venkatareddy1203)
- 🐙 [GitHub](https://github.com/venkata1236)


