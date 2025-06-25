import os
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader

CHROMA_DIR = "vector_store/db_store"

def load_documents(directory="data"):
    docs = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            loader = TextLoader(os.path.join(directory, filename))
            docs.extend(loader.load())
    return docs

def create_vector_store():
    documents = load_documents()
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = splitter.split_documents(documents)

    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma.from_documents(
        documents=texts,
        embedding=embedding,
        persist_directory=CHROMA_DIR
    )
    vectordb.persist()
    return vectordb

def load_vector_store():
    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return Chroma(persist_directory=CHROMA_DIR, embedding_function=embedding)

if __name__ == "__main__":
    if not os.path.exists(CHROMA_DIR):
        print("Creating new vector store...")
        create_vector_store()
    else:
        print("Loading existing vector store...")
        db = load_vector_store()
        results = db.similarity_search("What is Agentic AI?", k=2)
        for res in results:
            print(res.page_content)
