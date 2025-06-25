from agents.memory_agent import handle_memory

def get_registered_agents():
    return [
        {
            "name": "MemoryAgent",
            "description": "Handles memory logging and retrieval",
            "function": handle_memory
        }
    ]
