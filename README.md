# 📚 Simple RAG Application

A Retrieval-Augmented Generation (RAG) application built with **Python**, **Streamlit**, **LangChain**, and **Google Gemini**. The application allows users to upload documents, create a vector database, and ask questions based on the document content.

---

## 🚀 Features

* 📄 Upload PDF documents
* 🔍 Extract and process document text
* 🧩 Split text into chunks
* 🧠 Generate embeddings
* 💾 Store embeddings in a vector database
* 🤖 Retrieve relevant context using RAG
* 💬 Answer user queries using Google Gemini
* 🌐 Simple Streamlit-based user interface

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Google Gemini API
* ChromaDB (or your configured vector database)
* PyPDF
* Python Dotenv

---

## 📁 Project Structure

```text
.
├── ui.py              # Streamlit user interface
├── ingest.py          # Document ingestion and indexing
├── rag.py             # Retrieval and question-answering logic
├── requirements.txt
├── .env.example
├── README.md
├── data/              # PDF documents
└── chroma_db/         # Vector database (generated locally)
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<repository-name>.git
cd <repository-name>
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file and add your Gemini API key:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ Usage

### Step 1: Ingest Documents

```bash
python ingest.py
```

This processes the documents and creates the vector database.

### Step 2: Launch the Application

```bash
streamlit run ui.py
```

Open the displayed local URL in your browser.

---

## 📌 Workflow

1. Upload or place PDF documents in the `data/` folder.
2. Run `ingest.py` to create document embeddings.
3. Launch the Streamlit application.
4. Ask questions related to the uploaded documents.
5. The application retrieves relevant content and generates an answer using Google Gemini.

---

## 📷 Demo

You can add screenshots of the application here.

---

## 📄 Requirements

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🔒 Environment Variables

```env
GOOGLE_API_KEY=your_api_key_here
```

Do **not** commit your `.env` file to GitHub.

---

## 🤝 Contributing

Contributions, improvements, and suggestions are welcome. Feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.
