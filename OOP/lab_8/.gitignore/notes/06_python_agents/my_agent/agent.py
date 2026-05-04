from google.adk.agents.llm_agent import Agent
from google.genai.types import GenerateContentConfig

def build_story_idea(theme: str, mood: str = "таємничий") -> dict:
    """
    Створює ідею для історії
    
    Args:
        theme: тема історії
        mood: настрій (веселий, сумний, таємничий)
    
    Returns:
        dict: опис ідеї
    """
    prompt = f"Історія на тему '{theme}' з настроєм '{mood}'. Додай несподіваний сюжетний поворот."
    
    return {
        "theme": theme,
        "mood": mood,
        "story_prompt": prompt
    }

root_agent = Agent(
    model='gemini-2.5-flash',
    name='story_creator',
    description="Агент для створення креативних історій.",
    instruction="""
    Ти професійний письменник.
    
    Пиши історії, які:
    - мають захоплюючий сюжет
    - містять емоції та діалоги
    - мають логічний початок, середину та кінець
    - написані українською мовою
    
    Використовуй інструмент build_story_idea для створення основи історії,
    а потім розвивай її у повноцінну розповідь.
    """,
    tools=[build_story_idea],
    
    # Креативні налаштування (іншi, ніж у методичці)
    config=GenerateContentConfig(
        temperature=1.2,   # трохи менше хаосу, але все ще креативно
        top_k=50,
        top_p=0.9,
    )
)