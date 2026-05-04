from google.adk.agents.llm_agent import Agent
from tools.common_tools import format_text, count_words

def process_text(text: str) -> dict:
    formatted = format_text(text, "title")
    stats = count_words(text)
    
    return {
        "formatted_text": formatted,
        "stats": stats
    }

root_agent = Agent(
    model='gemini-2.5-flash',
    name='student_helper',
    description="Агент для роботи з текстом.",
    instruction="Використовуй process_text для аналізу тексту.",
    tools=[process_text],
)