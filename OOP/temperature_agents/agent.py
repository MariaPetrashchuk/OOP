from google.adk.agents.llm_agent import Agent
from google.genai.types import GenerateContentConfig

# 🔹 Агент-експерт (точний)
expert_agent = Agent(
    model='gemini-2.5-flash',
    name='expert_agent',
    description="Дає точні і короткі відповіді",
    instruction="Відповідай чітко, коротко і по факту українською мовою.",
    config=GenerateContentConfig(
        temperature=0.1,
    )
)

# 🔹 Агент-асистент (збалансований)
assistant_agent = Agent(
    model='gemini-2.5-flash',
    name='assistant_agent',
    description="Дає зрозумілі пояснення",
    instruction="Пояснюй просто і зрозуміло українською мовою.",
    config=GenerateContentConfig(
        temperature=0.7,
    )
)

# 🔹 Агент-письменник (креативний)
writer_agent = Agent(
    model='gemini-2.5-flash',
    name='writer_agent',
    description="Генерує креативні тексти",
    instruction="Пиши красиво, творчо і з уявою українською мовою.",
    config=GenerateContentConfig(
        temperature=1.3,
    )
)

# 🔹 Головний агент (щоб ADK бачив)
root_agent = assistant_agent