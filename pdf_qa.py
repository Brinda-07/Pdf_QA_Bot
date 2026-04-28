import streamlit as st
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate



llm = ChatGroq(
    api_key=st.secrets["GROQ_API_KEY"],
    model="llama-3.1-8b-instant"
)

@st.cache_resource
def load_embeddings():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

embeddings = load_embeddings()

def load_pdf(file):
    with open("temp.pdf", "wb") as f:
        f.write(file.read())
    loader = PyPDFLoader("temp.pdf")
    return loader.load()

def split_docs(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=100)
    return splitter.split_documents(docs)

def vectordb(chunks):
    return FAISS.from_documents(chunks, embeddings)

prompt = PromptTemplate(
    template="""
You are a helpful AI assistant.
Answer ONLY using the given context.
If answer not found say: NOT FOUND IN THE PDF

context: {context}
question: {question}
""",
    input_variables=["context", "question"]
)

st.title("📄 PDF Q&A Bot")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    st.success("PDF uploaded successfully!")

    if "vector_store" not in st.session_state or st.session_state.get("file_name") != uploaded_file.name:
        with st.spinner(" Reading PDF..."):
            docs = load_pdf(uploaded_file)
        with st.spinner(" Splitting..."):
            chunks = split_docs(docs)
        with st.spinner(" Storing the data..."):
            st.session_state.vector_store = vectordb(chunks)
            st.session_state.file_name = uploaded_file.name
        st.success("✅ Ready! Ask your question.")

    retriever = st.session_state.vector_store.as_retriever(search_kwargs={"k": 5})
    query = st.text_input("Ask a question from PDF")

    if query:
       with st.spinner(" Searching & generating answer..."):
            results = retriever.invoke(query)
            context = "\n\n".join([d.page_content for d in results])
            final_prompt = prompt.format(context=context, question=query)
            response = llm.invoke(final_prompt)

         # YEH DEKH
    
       st.write("### Answer:")
       st.write(response.content)