import streamlit as st

from modules.resume_generator import show_resume_generator
from modules.cover_letter import show_cover_letter
from modules.resume_analyzer import show_resume_analyzer

st.set_page_config(
    page_title="AI Resume Assistant",
    page_icon="📄",
    layout="wide"
)

# ---------------- Sidebar ---------------- #

st.sidebar.title("📄 AI Resume Assistant")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📄 Resume Generator",
        "✉️ Cover Letter Generator",
        "📊 Resume Analyzer",
        "ℹ️ About"
    ]
)

# ---------------- Home ---------------- #

if page == "🏠 Home":

    st.title("📄 AI Resume & Cover Letter Generator")

    st.markdown("---")

    st.header("Welcome!")

    st.write("""
This AI-powered application helps you create:

- 📄 ATS-Friendly Resume
- ✉️ Professional Cover Letter
- 📊 Resume Improvement Suggestions

Powered by Google Gemini.
""")

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("📄 Resume Generator")

    with col2:
        st.success("✉️ Cover Letter Generator")

    with col3:
        st.warning("📊 Resume Analyzer")

# ---------------- Resume Generator ---------------- #

elif page == "📄 Resume Generator":

    show_resume_generator()

# ---------------- Cover Letter ---------------- #

elif page == "✉️ Cover Letter Generator":

    show_cover_letter()

# ---------------- Resume Analyzer ---------------- #

elif page == "📊 Resume Analyzer":
    show_resume_analyzer()

# ---------------- About ---------------- #

elif page == "ℹ️ About":

    st.header("ℹ️ About")

    st.write("""
### AI Resume & Cover Letter Generator

Built using:

- 🐍 Python
- 🎈 Streamlit
- 🤖 Google Gemini AI
- 📄 ReportLab
- 📝 python-docx

This project generates ATS-friendly resumes and professional cover letters using Generative AI.
""")