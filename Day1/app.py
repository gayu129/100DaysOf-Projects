import streamlit as st
from fpdf import FPDF
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

# Resume Generator class
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'AI-Generated Resume', ln=True, align='C')

    def section_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, ln=True)

    def section_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 10, body)

def generate_pdf(name, email, phone, summary, skills, education, experience, filename="resume.pdf"):
    pdf = PDF()
    pdf.add_page()

    # Personal Info
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, name, ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 10, f"Email: {email} | Phone: {phone}", ln=True)
    pdf.ln(5)

    # Summary
    pdf.section_title("Professional Summary")
    pdf.section_body(summary)
    pdf.ln(5)

    # Skills
    pdf.section_title("Skills")
    pdf.section_body(', '.join(skills))
    pdf.ln(5)

    # Education
    pdf.section_title("Education")
    pdf.section_body(education)
    pdf.ln(5)

    # Experience
    pdf.section_title("Experience")
    pdf.section_body(experience)
    pdf.output(filename)

# Streamlit UI
st.set_page_config(page_title="AI Resume Builder", layout="centered")
st.title("📄 AI Resume Builder using NLP")

st.markdown("Fill in your details and click **Generate Resume**")

with st.form("resume_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    summary = st.text_area("Professional Summary")
    skills_input = st.text_input("Skills (comma-separated)")
    education = st.text_area("Education Background")
    experience = st.text_area("Work Experience")

    submit = st.form_submit_button("Generate Resume")

if submit:
    if not name or not email:
        st.warning("Please fill in at least Name and Email.")
    else:
        skills = [skill.strip() for skill in skills_input.split(",")]
        filename = f"{name.replace(' ', '_')}_resume.pdf"
        generate_pdf(name, email, phone, summary, skills, education, experience, filename)
        with open(filename, "rb") as file:
            st.success("🎉 Resume generated successfully!")
            st.download_button("📥 Download Resume PDF", file, file_name=filename)

