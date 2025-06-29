📄 PDF Question Answering App (Local LLM)

This project allows you to upload a PDF and ask questions about its content using a locally hosted language model (Flan-T5) and vector search powered by HuggingFace embeddings and FAISS.

🚀 Features

- 📄 Upload any PDF document
- 🔍 Ask contextual questions about its contents
- 🧠 Uses sentence-transformer (`all-MiniLM-L6-v2`) embeddings
- 🗂️ FAISS for efficient vector search
- 🤖 Local language model (`google/flan-t5-base`) for answering questions
- 💬 Multi-turn conversation support with session history
- 🧹 Clear chat option to reset conversation
  
🧱 Tech Stack

- Python 3.10+
- [Streamlit](https://streamlit.io/) - Web UI
- [LangChain](https://github.com/langchain-ai/langchain) - Chain and vector abstraction
- [FAISS](https://github.com/facebookresearch/faiss) - Vector similarity search
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- `PyMuPDF` - For extracting text from PDFs
- HuggingFace model: `google/flan-t5-base` (local)

📦 Installation
```bash
git clone https://github.com/your-username/pdf-qa-local.git
cd pdf-qa-local

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
If you're using a .env file for credentials (optional for HuggingFaceHub):

echo HF_TOKEN=your_token_here > .env


📁 Folder Structure
.
├── app.py                  # Streamlit app
├── utils.py                # PDF processing & QA logic
├── requirements.txt
└── README.md


🧪 Usage

streamlit run app.py
Upload a PDF file.

Ask any question about the content.

See contextual answers powered by local models.

Click "🧹 Clear Chat" to reset the conversation.

🧠 Models Used
Embedding Model
all-MiniLM-L6-v2 from SentenceTransformers

Converts PDF text chunks into numerical embeddings

Language Model
google/flan-t5-base (loaded locally via HuggingFace)

Generates answers from the retrieved context

📝 Requirements
Python >= 3.9

6GB+ RAM recommended

No external API usage – fully offline after setup

💡 Future Improvements
Support for larger models (e.g., flan-t5-large)

Upload and query across multiple PDFs

Highlight exact answers in PDF viewer

📜 License
This project is licensed under the MIT License. You are free to use, modify, and distribute.

🙌 Acknowledgments
HuggingFace Transformers
LangChain
FAISS

