# 📰 News Classifier & Summarizer

A Streamlit-based application that takes either text or image input, classifies the underlying news content into categories using a fine-tuned transformer model, and summarizes it using an LLM via Ollama.

This tool is designed for journalists, researchers, or anyone who wants to extract and quickly understand the essence of news articles — even from photos of printed media.

---

## ✨ Features

✅ Classify raw text into news categories  
✅ Extract text from images using OCR (Tesseract)  
✅ Summarize news using Ollama’s locally running models  
✅ Lightweight, fast, and privacy-friendly (runs locally)  
✅ Built using modern NLP and CV tools  

---

## 📦 Tech Stack

- [Streamlit](https://streamlit.io/) – Web app framework  
- [Hugging Face Transformers](https://huggingface.co/transformers) – Text classification  
- [Ollama](https://ollama.ai/) – Local LLM chat interface  
- [Pytesseract](https://github.com/madmaze/pytesseract) – OCR for image text extraction  
- [Pillow](https://python-pillow.org) – Image processing  

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/news-classifier-app.git
cd news-classifier-app

2. Install Dependencies
pip install -r requirements.txt

3. Install Tesseract-OCR
Add tesseract to your system PATH

4. Run Ollama and Load Model
Ensure Ollama is running and the required model (deepseek-r1:8b) is available: ollama run deepseek-r1:8b

5. Launch the App
bash
Copy
Edit
streamlit run app.py



📁 Project Structure

news-classifier-app/
├── app.py                   # Main Streamlit application
├── Classification_2_.ipynb  # main jupyter notebook ,for OCR->classification->summarisation
├── requirements.txt         # Python dependencies              
├── README.md                # This file
└── assets/                  # Sample images or visual assets




🧠 Future Improvements
Add support for multilingual OCR

Use hosted HuggingFace models for easier deployment

Export results as PDF/CSV

Add user feedback loop for improving classification

📜 License
This project is licensed under the MIT License – feel free to use, share, and modify with credit.

👨‍💻 Author
Manish
A curious mind exploring the intersection of language, learning, and logic.
Feel free to connect or contribute!

