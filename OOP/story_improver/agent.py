from google.adk.agents.llm_agent import Agent
from google.adk.agents.workflow.loop_agent import LoopAgent

# 🔹 Агент 1: генерує історію
generator = Agent(
    model='gemini-2.5-flash',
    name='generator',
    description="Створює історію",
    instruction="Напиши коротку історію на задану тему."
)

# 🔹 Агент 2: покращує історію
improver = Agent(
    model='gemini-2.5-flash',
    name='improver',
    description="Покращує текст",
    instruction="""
    Покращи історію:
    - додай емоції
    - зроби сюжет цікавішим
    - покращ стиль
    """
)

# 🔹 функція завершення циклу
def exit_loop(context) -> bool:
    # після 3 ітерацій зупиняємо цикл
    return context.iteration >= 3


# 🔹 Loop агент
root_agent = LoopAgent(
    name="story_improver",
    description="Агент, який покращує історію в циклі",
    agents=[generator, improver],
    exit_condition=exit_loop,
)