from google.adk.agents.llm_agent import Agent
from google.adk.agents.workflow.sequential_agent import SequentialAgent

# 🔹 Крок 1: генерація коду
generator = Agent(
    model='gemini-2.5-flash',
    name='generator',
    description="Генерує код",
    instruction="Створи Python функцію за запитом користувача."
)

# 🔹 Крок 2: перевірка коду
reviewer = Agent(
    model='gemini-2.5-flash',
    name='reviewer',
    description="Перевіряє код",
    instruction="Перевір код на помилки та запропонуй покращення."
)

# 🔹 Крок 3: покращення коду
refactor = Agent(
    model='gemini-2.5-flash',
    name='refactor',
    description="Покращує код",
    instruction="Виправ код і зроби його кращим та читабельним."
)

# 🔹 Sequential агент
root_agent = SequentialAgent(
    name="code_pipeline",
    description="Послідовний агент для генерації та покращення коду",
    agents=[generator, reviewer, refactor],
)