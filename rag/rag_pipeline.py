# rag/rag_pipeline.py

from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from core.llm_connector import get_llm
from vector_store.manager import load_vector_store

def build_rag_chain():
    llm = get_llm()
    retriever = load_vector_store().as_retriever()

    # Optional custom prompt (can be enhanced later)
    template = """
    Use the following context to answer the question concisely.
    Context:
    {context}

    Question: {question}
    """
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=template
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )
    return qa_chain

if __name__ == "__main__":
    rag = build_rag_chain()
    while True:
        query = input("\n🧠 Ask a question (or 'exit'): ")
        if query.lower() == "exit":
            break
        result = rag(query)
        print(f"\n🗨️ Answer:\n{result['result']}")
        print("\n📄 Source Docs:\n")
        for doc in result['source_documents']:
            print("-", doc.metadata['source'])
