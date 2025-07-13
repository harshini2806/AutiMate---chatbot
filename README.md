# 🌟 AutiMate — A Therapeutic Chatbot for Autistic Individuals

**AutiMate** is a web-based, retrieval-augmented AI chatbot designed to support individuals on the autism spectrum with emotionally safe, grounded, and context-aware conversations. It uses a document-based knowledge base, therapeutic prompting, and large language models to deliver supportive responses through a simple web interface.

---

## 🧠 Overview

AutiMate empowers autistic users by offering a calm and affirming space to talk, reflect, or seek information. Unlike generic chatbots, it retrieves factual content from curated Markdown files and adjusts its tone based on the user’s emotional or cognitive state via prompt modes.

Key capabilities include:

- Therapeutic tone customization with predefined support modes  
- Accurate, document-backed responses using RAG (Retrieval-Augmented Generation)  
- Local vector search with ChromaDB and MiniLM embeddings  
- Streamlit-based browser UI, no installation required for users  

---

## ⚙️ Architecture & Tech Stack

| Layer              | Technology Used |
|--------------------|-----------------|
| **Frontend UI**     | [Streamlit](https://streamlit.io/) |
| **Orchestration**   | [LangChain](https://www.langchain.com/) |
| **Language Model**  | `mistralai/Mixtral-8x7B-Instruct` via Hugging Face API |
| **Embedding Model** | `sentence-transformers/all-MiniLM-L6-v2` |
| **Vector DB**       | [Chroma](https://www.trychroma.com/) |
| **Data Format**     | Markdown (`.md`) |
| **Runtime**         | Python 3.10+ |
| **Environment Mgmt**| `python-dotenv` |

---

## 📁 Project Structure

```
autimate/
├── main.py                 # Streamlit app (chatbot interface)
├── chroma_storing.py       # Loads and stores embedded knowledge into Chroma
├── prompt_modes.py         # Custom prompt templates per support mode
├── data/autism/            # Markdown-based knowledge base
├── chroma/                 # Vector DB (auto-generated)
├── .env                    # Environment variables (e.g. HF API key)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 🚀 Quickstart Guide

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/autimate.git
cd autimate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file:

```env
HF_TOKEN=your_huggingface_api_token
```

### 4. Add Your Knowledge Base

Place your `.md` files inside the `data/autism/` directory. These are used to ground chatbot responses.

### 5. Generate Vector Embeddings

```bash
python chroma_storing.py
```

This script will:
- Load markdown files  
- Split them into chunks  
- Generate embeddings via MiniLM  
- Store them in Chroma for semantic search

### 6. Launch the Web App

```bash
streamlit run main.py
```

Visit [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🧘 Prompt Modes

AutiMate supports multiple interaction modes to match the user's emotional context. These are defined in `prompt_modes.py`.

| Mode                  | Description                                                                          |
|-----------------------|--------------------------------------------------------------------------------------|
| **Breakdown Support** | Gentle, validating tone for users in distress                                        |
| **Emotional Venting** | Non-judgmental, empathetic listener-style responses                                  |
| **Identity Reflection** | Supports self-discovery and affirmation of neurodivergent identity                  |
| **Casual Chat**       | Light, relaxed interaction with minimal structure                                    |
| **Learn About ASD**   | Informative responses grounded in markdown knowledge base                            |


---

## 💬 How It Works

1. **User sends a message** via the Streamlit interface  
2. **ChromaDB** retrieves top matching `.md` content based on semantic similarity  
3. **LangChain** builds a prompt using the selected mode and retrieved context  
4. **Hugging Face Endpoint** (Mixtral 8x7B) returns a natural-language response  
5. **Streamlit UI** renders the chat, tracking interaction history

---


## 📦 Dependencies

Your environment can be set up easily using the included `requirements.txt`. Below are the key libraries used:

### 🔧 Core Framework
- `streamlit` – for building the web UI

### 🧠 LangChain & LLM Orchestration
- `langchain`
- `langchain-community`
- `langchain-huggingface`
- `langchain-core`

### 📚 Vector Search & Embeddings
- `chromadb` – vector database
- `sentence-transformers` – MiniLM embedding model

### 🤗 Hugging Face Integration
- `huggingface-hub`
- `transformers`
- `accelerate` – required for many transformer-based models

### 🌐 Environment & File Support
- `python-dotenv` – for loading environment variables
- `markdown` – to read `.md` content

### 🧹 Utilities
- `tqdm` – progress bars/logging
- `protobuf==3.20.3` – specific version needed by Chroma or Hugging Face libs

---

### 📥 Install All Dependencies

```bash
pip install -r requirements.txt
```


## 📚 Acknowledgements
- This project acknowledges open-access autism resources for their role in awareness and support.
- The autistic community for shaping inclusive design principles  
- Hugging Face, LangChain, and Chroma teams for open AI tooling

---

