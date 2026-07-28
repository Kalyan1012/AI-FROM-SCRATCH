# 🚀 Day 5: AI Resume Evaluator & Candidate Ranker

Welcome to the Day 5 project of the AI Engineering course! 

The core code, Streamlit UI, and multi-document parsing pipeline developed for this assignment are maintained in the main **AI Resume Evaluator** repository.

---

## 🔗 Project Link

👉 **[Click here to view the full AI Resume Evaluator Repository](https://github.com/Kalyan1012/AI-Resume-Evaluator)**


---

## 📌 Project Overview

This project is an AI-powered HR tool that parses candidate resumes and ranks them against job descriptions:

* **Document Parsing**: Reads both `.pdf` and `.docx` resumes automatically.
* **Structured Outputs**: Uses **Pydantic** schemas to extract clean JSON data for candidate skills and experience.
* **Fast LLM Scoring**: Powered by **Groq API** (`openai/gpt-oss-120b`).
* **Interactive UI**: Built with **Streamlit** for drag-and-drop resume uploading and visual candidate ranking.

---

## 🛠️ Quick Run Instructions

If you are already in this folder, you can run the app directly:

```bash
# 1. Activate your virtual environment
source venv/bin/activate

# 2. Run the Streamlit web app
streamlit run resume_parser.py