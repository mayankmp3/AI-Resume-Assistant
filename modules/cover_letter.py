import streamlit as st
from modules.gemini_service import generate_response
from modules.pdf_generator import create_pdf


def show_cover_letter():

    st.title("✉️ AI Cover Letter Generator")

    st.markdown(
        "Generate a personalized, ATS-friendly cover letter using Google Gemini AI."
    )

    st.divider()

    # -----------------------
    # Personal Information
    # -----------------------

    st.subheader("👤 Personal Information")

    col1, col2 = st.columns(2)

    with col1:
        full_name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")

    with col2:
        job_role = st.text_input(
            "Target Job Role",
            placeholder="Data Analyst"
        )

        company = st.text_input(
            "Company Name",
            placeholder="Google"
        )

    st.divider()

    # -----------------------
    # Experience
    # -----------------------

    st.subheader("💼 Work Experience")

    experience = st.text_area(
        "Describe your work experience or internships",
        height=150,
        placeholder="Worked as a Data Analyst Intern where I built dashboards using Power BI..."
    )

    st.divider()

    # -----------------------
    # Skills
    # -----------------------

    st.subheader("🛠 Skills")

    skills = st.text_area(
        "Enter your skills (comma separated)",
        height=120,
        placeholder="Python, SQL, Machine Learning, Power BI, Excel"
    )

    st.divider()

    # -----------------------
    # Job Description
    # -----------------------

    st.subheader("📄 Job Description")

    job_description = st.text_area(
        "Paste the Job Description (Optional)",
        height=180
    )

    st.divider()

    # -----------------------
    # Additional Information
    # -----------------------

    st.subheader("✨ Additional Information")

    additional = st.text_area(
        "Achievements, certifications or anything you'd like to include (Optional)",
        height=120
    )

    st.divider()

    # -----------------------
    # Generate Button
    # -----------------------

    if st.button(
        "✨ Generate Cover Letter",
        use_container_width=True
    ):

        # Basic validation

        if not full_name or not email or not job_role or not company:

            st.warning(
                "Please fill in Full Name, Email, Target Job Role and Company Name."
            )

            return

        prompt = f"""
You are an expert HR recruiter and professional resume writer.

Generate a professional ATS-friendly cover letter.

Use ONLY the information provided below.

Candidate Information

Full Name:
{full_name}

Email:
{email}

Phone:
{phone}

Target Job Role:
{job_role}

Company Name:
{company}

Work Experience:
{experience}

Skills:
{skills}

Job Description:
{job_description}

Additional Information:
{additional}

Instructions:

1. Write a personalized cover letter.

2. Address the company using the provided company name.

3. Mention the target job role.

4. Explain why the candidate is a good fit.

5. Highlight the candidate's skills naturally.

6. Keep the tone professional and confident.

7. Length should be around 300–400 words.

8. DO NOT use placeholders like:
   [Company Name]
   [Target Job]
   [Phone Number]
   [Email]

9. Replace every placeholder with the actual candidate information.

10. Return ONLY the final cover letter.
"""

        with st.spinner("Generating Cover Letter..."):

            try:

                if cover_letter.startswith("Error"):

                    st.warning("⚠️ Gemini is temporarily unavailable.")
                    st.info("Showing Demo Cover Letter for presentation.")

                    cover_letter = f"""
                # Cover Letter

                **{full_name}**  
                {email}  
                {phone}

                Dear Hiring Manager,

                I am writing to express my interest in the {job_role} position at {company}.

                I have knowledge of {skills} and I am interested in applying these skills in a professional environment. My experience includes {experience if experience else "academic learning and project work"}.

                I am interested in this opportunity because it will allow me to contribute my knowledge, improve my practical skills, and learn from experienced professionals.

                {additional}

                Thank you for considering my application. I look forward to the opportunity to discuss my application further.

                Sincerely,  
                {full_name}
                """

                    st.warning("DEMO OUTPUT — This is a sample cover letter, not AI-generated.")

                st.success("Cover Letter Generated Successfully!")
                st.divider()
                st.subheader("📄 Cover Letter Preview")
                st.markdown(cover_letter)

                st.success("✅ Cover Letter Generated Successfully!")

                st.divider()

                st.subheader("📄 Cover Letter Preview")

                st.markdown(cover_letter)

                st.divider()

                # Create PDF
                pdf = create_pdf(cover_letter)

                col1, col2 = st.columns(2)

                with col1:
                    st.download_button(
                       label="📄 Download Cover Letter (PDF)",
                       data=pdf,
                       file_name="CoverLetter.pdf",
                       mime="application/pdf",
                       use_container_width=True
                    )

                with col2:
                    st.download_button(
                        label="📋 Download Cover Letter (.md)",
                        data=cover_letter,
                        file_name="CoverLetter.md",
                        mime="text/markdown",
                        use_container_width=True
                    )

            except Exception as e:

                st.error(f"Error: {e}")