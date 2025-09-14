# 🤖 Restaurant Chatbot - Automation Restaurant

## 📌 Introduction

This project builds an **intelligent restaurant chatbot**, using **RAG (Retrieval-Augmented Generation)** to provide accurate information for the LLM, integrated with **n8n** for workflow automation, and **Supabase** for storing + generating vector embeddings.  
Users can interact with the chatbot through a **Flask web interface** to get information about:

- Menu
- Promotions
- Table reservations
- Restaurant introduction
- Frequently asked questions

---

## ⚙️ Technologies Used

- **Python + Flask** → Web chat interface
- **LLM (Large Language Model)** → Natural language processing
- **RAG (Retrieval-Augmented Generation)** → Retrieve real data from the restaurant
- **Supabase** → Vector database for storing embeddings
- **n8n** → Workflow automation tool (manage requests, logs, APIs)
- **HTML + CSS** → Simple user interface (static & templates)

---

## 📂 Project Structure

```
AUTOMATION_RESTAURANT/
│── app.py                # Main Flask app
│── .env                  # Environment config (API keys, DB URL...)
│── requirements.txt      # Python dependencies
│── README.md             # Project documentation
│── My workflow.json      # n8n workflow
│
├── templates/
│   └── index.html        # Web interface
│
├── static/
│   ├── style.css         # UI styles
│   └── NhaHang.png       # Sample image
│
└── n8n-data/             # Workflow data and logs for n8n
```

---

## 🚀 Installation & Run

### 1. Clone the repo

```bash
git clone https://github.com/PeaIsPea/Automation_ChatBot_Restaurant.git
cd automation_restaurant
```

### 2. Create virtual environment & install dependencies

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/MacOS
.venv\Scripts\activate    # Windows

pip install -r requirements.txt
```

### 3. Setup environment variables

```
N8N_WEBHOOK_URL=http://localhost:5678/webhook/xxxxxx
```

### 4. Run Flask app

```bash
python app.py
```

App will run at:  
👉 http://127.0.0.1:5000

---

## 🔗 Workflow with n8n

The **`My workflow.json`** file contains the n8n workflow definition.  
It includes two main parts:

### 1. Chat Workflow

- Receive user queries from Flask via **Webhook**
- Pass the request to **AI Agent (Gemini + Memory)**
- Retrieve relevant knowledge from **Supabase Vector Store** (using HuggingFace embeddings)
- Format the response and **send it back to Flask** through the webhook

### 2. Knowledge Upload Workflow

- Triggered when the admin uploads a document (e.g., menu, FAQ, policy in PDF format)
- **Download & parse PDF** into text
- Split text into smaller chunks using **Recursive Character Text Splitter**
- Generate embeddings with **HuggingFace**
- Store vectors into **Supabase Vector Store** for later retrieval by the chatbot

---

## 📖 Features

- 💬 Chatbot helps customers book tables, ask about dishes, view promotions
- 🔎 Fast information retrieval with RAG + Supabase vectors
- ⚡ Workflow automation via n8n (reduce manual tasks)
- 🌐 Simple, user-friendly web interface

---

## 🏆 Future Improvements

- Integrate with **Zalo, Messenger**
- Connect to **POS ordering system**
- Build admin dashboard (Supabase + Flask Admin)

---

## 👨‍💻 Author

Developed by Pea.  
Goal: Automate restaurant workflows with AI + Automation + Modern Databases.
