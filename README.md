# 📸 Gemini Multimodal Image Description App

A simple, lightweight Python application that uses **Google Gemini 2.5 Flash** to:
- 🖼️ Upload images  
- 🤖 Generate detailed AI descriptions  
- 📝 Provide clean text outputs  
- 🌐 Interact through a Streamlit-based UI  

This project demonstrates how to integrate **Gemini's multimodal capabilities** with a user-friendly interface.

---

## 🚀 Features
### **1. Image Description**
Upload any JPG/PNG image and receive an AI‑generated detailed description.

### **2. Gemini API Integration**
Uses:
```python
from google import genai

📦 Installation
1️⃣ Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Set your API key
Create a file named GEMINI_API_KEY.env (already included in repo) or export environment variable:

export GEMINI_API_KEY="your_api_key"
4️⃣ Run the app
streamlit run app.py

📂 project
│── app.py                 # Streamlit UI
│── multimodal_test.py     # Backend multimodal test
│── test.py                # Simple "Say hello" test
│── test_image.jpg         # Sample image
│── test_image2.jpg        # Sample image
│── GEMINI_API_KEY.env     # API key file (not pushed to GitHub)
│── .gitignore             # Ignoring secrets/files
│── README.md              # This file
GEMINI_API_KEY=your_key_here

