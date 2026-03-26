import tempfile
from pathlib import Path
import os
import streamlit as st

# works locally (.env) and on cloud (st.secrets)
os.environ["OPENAI_API_KEY"] = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY", ""))


from crew.job_crew import JobApplicationCrew

# ---------- Page config ----------
st.set_page_config(
    page_title="Job Application Crew",
    page_icon="💼",
    layout="wide",
)

# ---------- Header ----------
st.title("💼 Job Application Crew")
st.markdown("**AI-powered CV Analyzer → Job Matcher → Cover Letter Writer**")
st.divider()

# ---------- Sidebar ----------
with st.sidebar:
    st.header("👤 Candidate Info")
    candidate_name = st.text_input("Your Full Name", placeholder="e.g. Venkata Reddy")
    st.divider()

    st.header("📄 Upload CV")
    uploaded_cv = st.file_uploader(
        "Upload your CV",
        type=["pdf", "docx", "txt"],
        help="Supported: PDF, DOCX, TXT"
    )
    if uploaded_cv:
        st.success(f"✅ {uploaded_cv.name} uploaded")

    st.divider()
    st.caption("Powered by CrewAI + OpenAI")

# ---------- Main area ----------
st.subheader("📋 Job Description")
job_description = st.text_area(
    "Paste the full job description here",
    height=250,
    placeholder="Copy and paste the job description you want to apply for..."
)

st.divider()

run_button = st.button("🚀 Run Job Application Crew", use_container_width=True)

# ---------- Run crew ----------
if run_button:
    # Validations
    if not candidate_name.strip():
        st.error("❌ Please enter your full name in the sidebar.")
        st.stop()

    if not uploaded_cv:
        st.error("❌ Please upload your CV in the sidebar.")
        st.stop()

    if not job_description.strip():
        st.error("❌ Please paste a job description.")
        st.stop()

    # Save uploaded file to temp path
    suffix = Path(uploaded_cv.name).suffix
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded_cv.read())
        tmp_path = tmp.name

    # Run agents
    with st.spinner("🤖 Agents are working... This may take 1-2 minutes."):
        try:
            crew = JobApplicationCrew()
            result = crew.run(
                cv_file_path=tmp_path,
                job_description=job_description,
                candidate_name=candidate_name,
            )
        except Exception as e:
            st.error(f"❌ Something went wrong: {str(e)}")
            st.stop()

    st.success("✅ Done! Here are your results.")
    st.divider()

    # ---------- Display results ----------
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("📊 CV Summary")
        st.markdown(result["cv_summary"])
        st.download_button(
            label="⬇️ Download CV Summary",
            data=result["cv_summary"],
            file_name="cv_summary.txt",
            mime="text/plain",
        )

    with col2:
        st.subheader("🎯 Job Match Report")
        st.markdown(result["match_report"])
        st.download_button(
            label="⬇️ Download Match Report",
            data=result["match_report"],
            file_name="match_report.txt",
            mime="text/plain",
        )

    with col3:
        st.subheader("✉️ Cover Letter")
        st.markdown(result["cover_letter"])
        st.download_button(
            label="⬇️ Download Cover Letter",
            data=result["cover_letter"],
            file_name="cover_letter.txt",
            mime="text/plain",
        )
