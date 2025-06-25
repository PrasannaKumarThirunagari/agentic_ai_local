from memory.memory_logger import get_memory_db

def search_memory(query: str, k: int = 3):
    db = get_memory_db()
    results = db.similarity_search(query, k=k)
    return [r.page_content for r in results]
