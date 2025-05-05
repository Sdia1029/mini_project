# 📝 Text Summarizer (Mini Project)

A web-based **Text Summarization** tool built using **Flask** and powered by **LLaMA 3 8B** via the **Groq API**. This application allows users to input long text and receive a concise and meaningful summary.

---

## 🔍 Overview

This mini project uses prompt engineering techniques to generate a high-quality summary of user input text. It’s ideal for students, researchers, or anyone needing to quickly understand the core message of large content.

---

## ✨ Features

- 🧠 **AI-Powered**: Uses LLaMA 3 via Groq API for fast and smart summaries.
- ⚙️ **Flask Web App**: Simple and interactive web interface.
- 📄 **HTML Template**: A clean `index.html` page inside the `templates` folder.
- 🧾 **Neutral & Concise Summaries**: Eliminates repetition and focuses on the main ideas.

---

## 🧰 Technologies Used

- **Frontend**: HTML/CSS (`templates/index.html`)
- **Backend**: Flask
- **AI Model**: LLaMA 3 8B (via `langchain_groq`)
- **Prompt Handling**: LangChain

---

## 📁 Project Structure

```
Text-Summarizer/
├── app.py
├── templates/
│   └── index.html
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/Sdia1029/Text-Summarizer.git
cd Text-Summarizer
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # For Windows
# source venv/bin/activate  # For Mac/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Groq API Key

Replace the placeholder key in `app.py` with your own Groq API key:

```python
groq_api_key = "your_actual_api_key"
```

### 5. Run the App

```bash
python app.py
```

### 6. Open in Browser

Navigate to [http://127.0.0.1:5000/chat](http://127.0.0.1:5000/chat) to use the summarizer.

---

## 📌 Example Use

> Input:
```
Artificial intelligence (AI) is transforming industries from healthcare to finance...
```

> Output:
```
AI is revolutionizing various sectors like healthcare and finance through automation and data-driven insights.
```

---

## 📃 Prompt Logic

The summarization prompt is engineered to:
- Focus on key points.
- Avoid filler or repetition.
- Be understandable to new readers.
- Maintain original context and tone.

---

## 👩‍💻 Author

**Sadia Eman**  
BS Data Science |  Superior University

---
