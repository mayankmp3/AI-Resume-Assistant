import streamlit as st
from modules.gemini_service import generate_response
from modules.pdf_generator import create_pdf


def show_resume_generator():

    st.title("📄 AI Resume Generator")
    st.caption("Generate a professional ATS-friendly resume using Google's Gemini AI.")

    st.divider()

    # -------------------------
    # Personal Information
    # -------------------------
    st.subheader("👤 Personal Information")

    col1, col2 = st.columns(2)

    with col1:
        full_name = st.text_input("Full Name *")
        email = st.text_input("Email *")
        phone = st.text_input("Phone Number")

    with col2:
        linkedin = st.text_input("LinkedIn URL")
        github = st.text_input("GitHub URL")
        portfolio = st.text_input("Portfolio Website")

    st.divider()

    # -------------------------
    # Education
    # -------------------------
    st.subheader("🎓 Education")

    degree = st.text_input("Degree")
    college = st.text_input("College / University")

    col1, col2 = st.columns(2)

    with col1:
        graduation_year = st.text_input("Graduation Year")

    with col2:
        cgpa = st.text_input("CGPA / Percentage")

    st.divider()

    # -------------------------
    # Skills
    # -------------------------
    st.subheader("💻 Skills")

    skills = st.text_area(
        "Skills (comma separated)",
        placeholder="Python, SQL, Power BI, Machine Learning"
    )

    st.divider()

    # -------------------------
    # Experience
    # -------------------------
    st.subheader("💼 Experience")

    experience = st.text_area(
        "Work Experience / Internship",
        height=150
    )

    st.divider()

    # -------------------------
    # Projects
    # -------------------------
    st.subheader("🚀 Projects")

    projects = st.text_area(
        "Projects",
        height=150
    )

    st.divider()

    # -------------------------
    # Certifications
    # -------------------------
    st.subheader("🏆 Certifications")

    certifications = st.text_area(
        "Certifications",
        height=120
    )

    st.divider()

    # -------------------------
    # Target Job
    # -------------------------
    st.subheader("🎯 Target Job")

    target_job = st.text_input(
        "Target Job Role",
        placeholder="Data Analyst"
    )

    st.divider()

    generate = st.button(
        "✨ Generate Resume",
        use_container_width=True
    )

    # ===========================================================
    # Generate Resume
    # ===========================================================

    if generate:

        # Basic Validation

        if full_name.strip() == "":
            st.error("Please enter your Full Name.")
            return

        if email.strip() == "":
            st.error("Please enter your Email.")
            return

        prompt = f"""
You are a Senior HR Recruiter with 15+ years of hiring experience.

Your task is to create a professional, ATS-friendly resume.

Rules:

1. Never invent information.

2. Use ONLY the information provided.

3. Skip empty sections.

4. Keep the resume professional.

5. Use strong action verbs.

6. Make it ATS Optimized.

7. Return the resume in clean Markdown.

8. Organize sections in this order:

# Full Name

Contact Information

Professional Summary

Education

Technical Skills

Experience

Projects

Certifications

Candidate Information

Full Name:
{full_name}

Email:
{email}

Phone:
{phone}

LinkedIn:
{linkedin}

GitHub:
{github}

Portfolio:
{portfolio}

Degree:
{degree}

College:
{college}

Graduation Year:
{graduation_year}

CGPA:
{cgpa}

Skills:
{skills}

Experience:
{experience}

Projects:
{projects}

Certifications:
{certifications}

Target Job:
{target_job}

Generate the complete resume.
"""

        with st.spinner("🤖 Gemini is writing your ATS Resume..."):

            resume = generate_response(prompt)

        if resume.startswith("Error"):

            st.warning("⚠️ Gemini is temporarily unavailable.")
            st.info("Showing Demo Resume so you can demonstrate the application.")

            resume = f"""
        # {full_name}

        Email: {email}
        Phone: {phone}

        LinkedIn: {linkedin}
        GitHub: {github}
        Portfolio: {portfolio}

        ## Professional Summary

        Motivated candidate seeking opportunities as a {target_job}.
        Interested in applying skills and learning through professional experience.

        ## Education

        **{degree}**
        {college}

        Graduation Year: {graduation_year}
        CGPA: {cgpa}

        ## Skills

        {skills}

        ## Experience

        {experience if experience else "No experience provided."}

        ## Projects

        {projects if projects else "No projects provided."}

        ## Certifications

        {certifications if certifications else "No certifications provided."}
        """

            st.warning("DEMO OUTPUT — This is a sample resume, not AI-generated.")

        st.success("✅ Resume Generated Successfully!")

        st.divider()

        st.markdown("## 📄 Resume Preview")

        st.markdown(resume)

        st.divider()

        # Generate PDF
        pdf = create_pdf(resume)

        col1, col2 = st.columns(2)

        with col1:
          st.download_button(
              "📄 Download Resume (PDF)",
              data=pdf,
              file_name="Resume.pdf",
              mime="application/pdf",
              use_container_width=True,
           )

        with col2:
          st.download_button(
              "📋 Download Resume (.md)",
              data=resume,
              file_name="Resume.md",
              mime="text/markdown",
              use_container_width=True,
           )