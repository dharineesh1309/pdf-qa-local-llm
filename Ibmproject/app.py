import streamlit as st
from utils import extract_text_from_pdf, create_vectorstore, ask_question

st.set_page_config(page_title="PDF Q&A", layout="wide")
st.title("📄 Ask Your PDF")

# --- Session State Initialization ---
if "conversation" not in st.session_state:
    st.session_state.conversation = []
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

# --- File Upload ---
pdf = st.file_uploader("Upload your PDF", type="pdf")

if pdf and st.session_state.vectorstore is None:
    with st.spinner("Processing PDF..."):
        text = extract_text_from_pdf(pdf)
        st.session_state.vectorstore = create_vectorstore(text)
    st.success("PDF processed. You can start asking questions.")

# --- Clear Chat Button ---
if st.button("🧹 Clear Chat"):
    st.session_state.conversation = []

# --- Question Input ---
question = st.text_input("Ask a question about the PDF:")

if question and st.session_state.vectorstore:
    with st.spinner("Thinking..."):
        answer = ask_question(st.session_state.vectorstore, question)
        st.session_state.conversation.append({"question": question, "answer": answer})

# --- Display Chat History ---
if st.session_state.conversation:
    st.subheader("🧠 Chat History")
    for qa in reversed(st.session_state.conversation):  # Latest first
        st.markdown(f"**🧍 You:** {qa['question']}")
        st.markdown(f"**🤖 AI:** {qa['answer']}")
        st.markdown("---")
