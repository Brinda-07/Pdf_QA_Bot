# 📄 PDF RAG Chatbot

An AI-powered chatbot that allows users to upload PDF documents and ask questions in natural language. The system uses Retrieval-Augmented Generation (RAG) to provide accurate, context-aware answers from the uploaded document.

---

## 🧠 Features

* 📂 Upload any PDF document
* 🔍 Semantic search using FAISS
* 🤖 Context-aware answers using LLM (Groq)
* 🧩 Document chunking & embeddings
* ⚡ Fast and interactive Streamlit UI
* ❌ Fallback when answer not found in document

---

## 🏗️ Tech Stack

* **Language:** Python
* **Frameworks & Libraries:** LangChain, Streamlit
* **Vector Database:** FAISS
* **Embeddings:** HuggingFace (sentence-transformers)
* **LLM:** Groq (LLaMA 3)
* **PDF Processing:** PyPDF

---

## ⚙️ How It Works

1. User uploads a PDF
2. PDF is split into smaller chunks
3. Chunks are converted into embeddings
4. Stored in FAISS vector database
5. User asks a question
6. Relevant chunks are retrieved
7. Context + question → passed to LLM
8. LLM generates final answer

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Brinda-07/Pdf_QA_Bot.git
cd Pdf_QA_Bot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add API Key

Create a `.env` file and add:

```
GROQ_API_KEY=your_api_key_here
```

*(For Streamlit Cloud, add it in Secrets instead)*

### 4. Run the app

```bash
streamlit run pdf_qa.py
```

---

## 📸 Demo

<img width="791" height="532" alt="Screenshot 2026-04-28 194541" src="https://github.com/user-attachments/assets/dae8ebc4-1398-4203-963b-31a85095fddd" />


<img width="804" height="490" alt="Screenshot 2026-04-28 195841" src="https://github.com/user-attachments/assets/00290959-9db8-4758-8ee9-1f99b46549e5" />

---




