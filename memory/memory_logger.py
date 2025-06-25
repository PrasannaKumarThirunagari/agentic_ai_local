import os
import uuid
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_core.documents import Document

MEMORY_DB_DIR = "memory/mem_db"

def get_memory_db():
    embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    return Chroma(persist_directory=MEMORY_DB_DIR, embedding_function=embedding)

def log_memory(text: str):
    doc = Document(
        page_content=text.strip(),
        metadata={"id": str(uuid.uuid4())}
    )
    db = get_memory_db()
    db.add_documents([doc])
    db.persist()
    return "✅ Memory logged."
