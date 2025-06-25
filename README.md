# 🧠 Agentic AI — Fully Local, Modular AI Assistant

A privacy-first, fully local, CPU-friendly **Agentic AI System** using:

- 🧱 Multi-Agent Architecture
- 🧠 RAG (Retrieve-Augment-Generate)
- 💬 LLM (LLaMA3 via Ollama)
- 📁 Vector DB (ChromaDB + Sentence Transformers)
- 🧭 MCP (Memory & Context Processor)
- 🌐 UI with Streamlit

---

## 🚀 Tech Stack

| Component            | Library / Tool              | Version      |
|---------------------|-----------------------------|--------------|
| Language             | Python                      | >=3.10       |
| Virtual Env         | venv                        | -            |
| Agent Framework     | LangChain                   | >=0.2.0      |
| LLM Runtime         | Ollama                      | >=0.5.1      |
| Model               | LLaMA 3 (via Ollama)        | llama3       |
| Vector Store        | ChromaDB                    | >=0.4.0      |
| Embeddings          | sentence-transformers       | all-MiniLM-L6-v2 |
| UI                  | Streamlit                   | >=1.35.0     |

---

## 📁 Project Structure

```
agentic_ai_local/
├── agents/
│   ├── memory_agent.py
│   └── agent_registry.py
├── core/
│   └── llm_connector.py
├── memory/
│   ├── memory_logger.py
│   └── memory_retriever.py
├── mcp/
│   └── mcp_controller.py
├── ui/
│   └── streamlit_app.py
├── requirements.txt
├── README.md
```

---

## 🛠️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/agentic_ai_local.git
cd agentic_ai_local
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
# Activate venv:
venv\Scripts\activate    # Windows
# OR
source venv/bin/activate  # Linux/macOS
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Install and run Ollama
- Download from https://ollama.com
- Then run:
```bash
ollama pull llama3
```

---

## ▶️ Run the App

```bash
streamlit run ui/streamlit_app.py
```

> 🧠 The app opens in your browser at http://localhost:8501

---

## 🧪 Test Prompts

### Log some memory:
```
note I slept 6 hours last night
note I drank 3 liters of water today
remember I went to Goa in 2022
```

### Retrieve them:
```
how much did I sleep?
what did I drink?
where did I go in 2022?
```

> 💬 Recent memories are visible in the "🧠 Memory Logs" tab.

---

## 🔧 Available Agents (Default)

| Agent Name   | Function |
|--------------|----------|
| MemoryAgent  | Logs & retrieves memory from vector DB |
| CalculatorAgent (optional) | Performs basic math |
| [You can add more easily] |

To add new agents, modify:
```python
# agents/agent_registry.py
{
  "name": "MyNewAgent",
  "function": handle_my_new_agent
}
```

---

## 🗂️ Requirements File

```txt
streamlit
langchain>=0.2.0
langchain-community
langchain-ollama
langchain-chroma
langchain-huggingface
sentence-transformers
transformers
chromadb
ollama
```

---

## ✨ Features

- ✅ Fully Offline, CPU-efficient
- 🧠 Modular Multi-Agent System
- 🔎 Vector Memory Search (RAG)
- 🔒 No cloud, all local
- 💬 Clean UI via Streamlit
- 🧩 Easy to extend (add agents)

---

## 📄 License

MIT License — use freely, credit appreciated.

---

## 🙋‍♂️ Author

Built with ❤️ by **Damodar** — AI Architect & .NET Fullstack Dev
