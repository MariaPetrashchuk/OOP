from google.adk.agents.llm_agent import Agent
from tools.common_tools import format_text

def shout(text: str) -> dict:
    return {"result": format_text(text, "uppercase")}

root_agent = Agent(
    model='gemini-2.5-flash',
    name='text_formatter',
    description="Форматує текст.",
    instruction="Використовуй shout для форматування тексту.",
    tools=[shout],
)
