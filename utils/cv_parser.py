"""
cv_parser.py
------------
Extracts raw text from PDF, DOCX, or TXT resume files.
Skill extraction is handled by the LLM agent — no hardcoded keywords.
"""


from pathlib import Path
from typing import Dict

import docx
from PyPDF2 import PdfReader


def extract_text_from_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    pages = [page.extract_text() or "" for page in reader.pages]
    return "\n".join(pages)


def extract_text_from_docx(file_path: str) -> str:
    doc = docx.Document(file_path)
    paras = [p.text for p in doc.paragraphs if p.text.strip()]
    return "\n".join(paras)


def extract_cv_text(file_path: str) -> str:
    path = Path(file_path)
    suffix = path.suffix.lower()

    if suffix == ".pdf":
        return extract_text_from_pdf(str(path))
    if suffix in {".docx", ".doc"}:
        return extract_text_from_docx(str(path))

    # fallback for plain text files
    return path.read_text(encoding="utf-8", errors="ignore")


def simple_cv_summary(raw_text: str) -> Dict:
    """
    Lightweight pre-processing only.
    Skill extraction is handled by the CV Analyst LLM agent — works for ANY role/domain.
    """
    lines = [l.strip() for l in raw_text.splitlines() if l.strip()]

    return {
        "raw_text": raw_text,
        "name_guess": lines[0] if lines else "Unknown",
        "experience_snippet": "\n".join(lines[:30]),
    }
