import streamlit as st
from modules.gemini_service import generate_response


def show_resume_analyzer():

    st.title("📊 AI Resume Analyzer")

    st.markdown(
        "Upload or paste your resume and get AI-powered professional feedback."
    )

    st.divider()

    option = st.radio(
        "Choose Input Method",
        ["📄 Paste Resume", "📁 Upload Resume (.txt)"],
        horizontal=True
    )

    resume_text = ""

    if option == "📄 Paste Resume":

        resume_text = st.text_area(
            "Paste your Resume",
            height=350,
            placeholder="Paste your complete resume here..."
        )

    else:

        uploaded_file = st.file_uploader(
            "Upload Resume (.txt)",
            type=["txt"]
        )

        if uploaded_file is not None:
            resume_text = uploaded_file.read().decode("utf-8")

            st.success("Resume uploaded successfully!")

    st.divider()

    target_job = st.text_input(
        "Target Job Role",
        placeholder="Example: Data Analyst"
    )

    st.divider()

    if st.button(
        "🔍 Analyze Resume",
        use_container_width=True
    ):

        if resume_text.strip() == "":
            st.warning("Please upload or paste your resume.")
            return

        prompt = f"""
You are a Senior HR Recruiter and Resume Reviewer.

Analyze the following resume for the role of:

{target_job}

Resume:

{resume_text}

Give your response in the following markdown format.

# Overall Review

Give 4-5 sentences about the resume.

# Strengths

List 5 strengths.

# Weaknesses

List 5 weaknesses.

# Missing Skills

Mention important skills that are missing for this job.

# Suggestions

Give at least 8 professional suggestions.

# Improved Professional Summary

Rewrite the professional summary.

# Final Verdict

Would you shortlist this candidate?
Explain why.
"""

        with st.spinner("Analyzing Resume..."):

            analysis = generate_response(prompt)

        st.success("Analysis Completed!")

        st.markdown(analysis)

        st.download_button(
            "📥 Download Analysis",
            analysis,
            file_name="resume_analysis.md",
            mime="text/markdown",
            use_container_width=True
        )