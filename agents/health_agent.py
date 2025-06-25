def log_health(query: str) -> str:
    # Example: basic keyword check (you can later embed & store logs)
    if "sleep" in query:
        return "Logged: You mentioned sleep. Sleep is essential for recovery."
    elif "water" in query:
        return "Logged: Water intake noted. Stay hydrated!"
    else:
        return "Health log received: " + query
