from dotenv import load_dotenv
import io
import base64
import streamlit as st
import os
from PIL import Image
import pdf2image
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google Gemini API
genai.configure(api_key="AIzaSyDFdkigE5Tkp0E5YnjnF0sT_kyrAikUMV8")

# Gemini response handler
def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')  # or use 'gemini-1.5-flash' for faster response
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

# PDF to image setup function
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert PDF to images using Poppler path
        images = pdf2image.convert_from_bytes(
            uploaded_file.read(),
            poppler_path=r"C:\Users\MUSTAFA\Downloads\poppler-24.08.0\Library\bin"
        )

        first_page = images[0]

        # Convert image to base64-encoded JPEG bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit UI
st.set_page_config(page_title="ATS Analyst")
st.header("ATS Resume Evaluator")

input_text = st.text_area("Job Description:", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF format)", type=["pdf"])

if uploaded_file is not None:
    st.success("✅ Resume uploaded successfully!")

# Buttons
submit1 = st.button("📄 Tell me about the resume")
submit3 = st.button("📊 Percentage Match")

# Prompts
input_prompt1 = """
You are an experienced HR professional with technical expertise in the fields of Data Science, Full Stack Web Development, Big Data Engineering, DevOps, and Data Analysis.
Your task is to review the provided resume in relation to the job description for these roles.
Please share your professional evaluation on whether the candidate's profile aligns with the requirements of the position. Highlight the strengths and weaknesses of the applicant in relation to the specified job role.
"""

input_prompt3 = """
You are a Technical Human Resource Analyst with experience in hiring for roles such as Data Scientist, Full Stack Developer, Big Data Engineer, DevOps Engineer, and Data Analyst.

Your task is to evaluate the provided resume against the job description and calculate an estimated **percentage match** based on the alignment of key skills, qualifications, experience, and responsibilities mentioned in both.

Please do the following:
1. **Calculate a percentage match** (0 - 100%) representing how well the resume fits the job description.
2. **Justify the match score** with a brief explanation of:
   - Key skills that are well aligned.
   - Important gaps or mismatches.
3. Provide suggestions, if any, on how the candidate can improve their profile to better match the role.
"""

# Actions
if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("🧾 Gemini Response")
        st.write(response)
    else:
        st.error("❌ Please upload a PDF resume.")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("📈 Match Score and Suggestions")
        st.write(response)
    else:
        st.error("❌ Please upload a PDF resume.")
