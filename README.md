# Bart Large CNN Summarizer
This project is a desktop-based application that allows users to simulate a chat environment and summarize the entire conversation using modern Natural Language Processing techniques. It is designed to help users quickly grasp the essence of long chat threads without having to read every message.

## 🚀 Features

- 🧠 Abstractive text summarization using Hugging Face's BART model
- 💻 Simple and intuitive chat-like GUI built with Python Tkinter
- ⚡ Fast and lightweight, works offline after setup
- 📝 Real-time message entry and summary generation
- 🔧 Easy to install and run locally

## 🛠️ Tech Stack

- **Frontend**: Python Tkinter
- **Backend (NLP)**: Hugging Face Transformers (BART model)
- **Language**: Python 3.7+

## 📸 Glimpse of the UI

Below is screenshot showcasing the user interface and summarization output:
<center>  
<img width="500" alt="Screenshot 2025-04-17 at 4 39 57 PM" src="https://github.com/user-attachments/assets/2fc3251f-f3cf-4c76-8402-77dafe02fd0d" />
</center>


## 📥 Installation

### 1. Create and activate a virtual environment:


```shell
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 2. Install the required packages:

```shell
pip install -r requirements.txt
```

### 3. Run the application:

```shell
python main.py
```

## 📁 File Structure 

```
.
├── LICENSE
├── README.md
├── __pycache__
│   └── summarizer.cpython-312.pyc
├── app.py
├── file_structure
├── requirements.txt
└── summarizer.py

2 directories, 7 files
```

## 🤖 Model Info

This project uses the BART-large CNN summarization model from Hugging Face:
`facebook/bart-large-cnn`

## 📃 License

This project is licensed under the GNU GENERAL PUBLIC LICENSE. 
