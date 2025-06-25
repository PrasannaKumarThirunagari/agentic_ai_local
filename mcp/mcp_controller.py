from agents.agent_registry import get_registered_agents

class MCP:
    def __init__(self):
        self.agents = get_registered_agents()

    def route(self, query: str) -> str:
        for agent in self.agents:
            result = agent["function"](query)
            if result:
                return result
        return "🤖 No agent could handle your query."
