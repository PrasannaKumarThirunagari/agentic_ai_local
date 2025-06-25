import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from mcp.mcp_controller import MCP
from memory.memory_logger import get_memory_db

# UI Setup
st.set_page_config(page_title="🧠 Agentic AI", page_icon="🧠")
st.title("🧠 Agentic AI — Local Assistant")

# Tabs: Chat + Memory Logs
tab1, tab2 = st.tabs(["💬 Chat", "🧠 Memory Logs"])

# ----- 💬 TAB 1: Chat -----
with tab1:
    if "mcp" not in st.session_state:
        st.session_state.mcp = MCP()
        st.session_state.chat_history = []

    user_input = st.chat_input("Ask me anything (math, health, memory, or general)...")

    if user_input:
        mcp = st.session_state.mcp
        response = mcp.route(user_input)

        st.session_state.chat_history.append(("🧑‍💻 You", user_input))
        st.session_state.chat_history.append(("🤖 Agentic AI", response))

    for speaker, message in st.session_state.chat_history:
        with st.chat_message("user" if speaker == "🧑‍💻 You" else "ai"):
            st.markdown(f"**{speaker}:** {message}")

# ----- 🧠 TAB 2: Memory Logs -----
with tab2:
    st.subheader("Your Logged Memories")

    db = get_memory_db()
    all_memories = db.get()["documents"]

    if all_memories:
        # Show recent memories first
        recent_memories = list(reversed(all_memories))
        for i, doc in enumerate(recent_memories):
            st.markdown(f"**{i+1}.** {doc}")
    else:
        st.info("No memory logs found yet. Try logging via the chat: `note I slept 6 hours`")