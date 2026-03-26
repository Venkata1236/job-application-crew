import os
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

from crew.job_crew import JobApplicationCrew


def validate_cv_path(path: str) -> bool:
    p = Path(path)
    return p.exists() and p.suffix.lower() in {".pdf", ".docx", ".doc", ".txt"}


def get_multiline_input(prompt: str) -> str:
    print(prompt)
    print("(Press Enter twice when done)\n")
    lines = []
    while True:
        line = input()
        if not line.strip() and lines:
            break
        lines.append(line)
    return "\n".join(lines)


def main():
    print("=" * 60)
    print("       JOB APPLICATION CREW — AI Powered Assistant")
    print("=" * 60)

    # --- CV path ---
    cv_path = input("\n📄 Enter path to your CV (.pdf / .docx / .txt):\n> ").strip()
    while not validate_cv_path(cv_path):
        print("❌ File not found or unsupported format. Try again.")
        cv_path = input("> ").strip()
    print("✅ CV loaded.\n")

    # --- Job description ---
    job_description = get_multiline_input("📋 Paste the Job Description:")
    if not job_description.strip():
        print("❌ Job description cannot be empty. Exiting.")
        sys.exit(1)
    print("✅ Job description received.\n")

    # --- Candidate name ---
    candidate_name = input("👤 Your full name (for cover letter):\n> ").strip()
    if not candidate_name:
        print("❌ Name cannot be empty. Exiting.")
        sys.exit(1)
    print("✅ Name saved.\n")

    # --- Run crew ---
    print("\n🚀 Starting Job Application Crew...\n")
    print("=" * 60)

    crew = JobApplicationCrew()
    result = crew.run(
        cv_file_path=cv_path,
        job_description=job_description,
        candidate_name=candidate_name,
    )

    # --- Display results ---
    print("\n" + "=" * 60)
    print("📊  CV SUMMARY")
    print("=" * 60)
    print(result["cv_summary"])

    print("\n" + "=" * 60)
    print("🎯  JOB MATCH REPORT")
    print("=" * 60)
    print(result["match_report"])

    print("\n" + "=" * 60)
    print("✉️   COVER LETTER")
    print("=" * 60)
    print(result["cover_letter"])

    # --- Save outputs to files ---
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    (output_dir / "cv_summary.txt").write_text(result["cv_summary"], encoding="utf-8")
    (output_dir / "match_report.txt").write_text(result["match_report"], encoding="utf-8")
    (output_dir / "cover_letter.txt").write_text(result["cover_letter"], encoding="utf-8")

    print("\n✅ All outputs saved to /outputs folder.")
    print("=" * 60)


if __name__ == "__main__":
    main()
