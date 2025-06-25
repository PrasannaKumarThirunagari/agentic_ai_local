from memory.memory_logger import log_memory
from memory.memory_retriever import search_memory
from core.llm_connector import get_llm

llm = get_llm()

def handle_memory(query: str) -> str:
    if any(kw in query.lower() for kw in ["remember", "log", "note", "store"]):
        return log_memory(query)

    if any(kw in query.lower() for kw in ["recall", "search", "how", "what", "did i", "past", "when", "who"]):
        memories = search_memory(query)
        if not memories:
            return "🧠 No memory found."

        context = "\n".join(memories)
        prompt = f"""
You are my memory assistant.

Based on the following memory logs, answer the user's question clearly and concisely.

### Memory Logs:
{context}

### User's Question:
{query}

### Answer:"""

        return llm.invoke(prompt)

    return "🤔 This doesn't look like a memory-related query."
