# 🧾 ATS Resume Evaluator using Gemini API

A smart Streamlit application that evaluates a candidate's resume against a job description using **Google's Gemini 1.5** models. It provides instant feedback on how well the resume aligns with the role and suggests areas for improvement — helping candidates optimize their chances of getting shortlisted.

---

## 🚀 Features

- 📄 Upload your resume in PDF format.
- 📝 Input a job description you're targeting.
- ✅ Get a professional evaluation of your resume.
- 📊 Get a **percentage match** score with reasoning and improvement suggestions.
- 🤖 Powered by **Gemini 1.5 Pro** via Google’s Generative AI API.

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MUSTAFAOP29/ATS-System.git
   cd ATS-System

2. (Optional but recommended) Create a virtual environment:
python -m venv venv
venv\Scripts\activate   # On Windows

3. Install dependencies
   pip install -r requirements.txt

🔐 Setup API Key
To use the Gemini API, you’ll need a Google API key:
1. Go to Google AI Studio and generate your API key.
2. Create a file named .env in the project root:
   GOOGLE_API_KEY=your_api_key_here


▶️ Run the App
Make sure your virtual environment is activated and run:
      streamlit run app.py
Then open your browser and go to: http://localhost:8501


📁 Project Structure

ATS-System/
│
├── app.py               # Main Streamlit application
├── requirements.txt     # List of dependencies
├── .env                 # Contains your Gemini API key (DO NOT SHARE)
└── README.md            # Project documentation


🖼️ Example Output
Input: Resume PDF + Job Description
Percentage Match: 78%
✔️ Good alignment with Data Science fundamentals
❌ Lacks project experience in MLOps and large-scale deployments

Suggestions:
- Add projects involving model deployment (e.g., using Docker, CI/CD)
- Highlight achievements using data visualization or dashboards


👨‍💻 Author
Made with ❤️ by Syed Mustafa
