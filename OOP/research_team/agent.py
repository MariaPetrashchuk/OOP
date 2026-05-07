from google.adk.agents.llm_agent import Agent
from google.adk.agents.workflow.parallel_agent import ParallelAgent

# 🔹 Агент 1: досліджує AI
ai_researcher = Agent(
    model='gemini-2.5-flash',
    name='ai_researcher',
    description="Досліджує AI",
    instruction="Опиши сучасні тренди у штучному інтелекті."
)

# 🔹 Агент 2: досліджує веб
web_researcher = Agent(
    model='gemini-2.5-flash',
    name='web_researcher',
    description="Досліджує веб",
    instruction="Опиши тренди у веб-розробці."
)

# 🔹 Агент 3: досліджує мобільні технології
mobile_researcher = Agent(
    model='gemini-2.5-flash',
    name='mobile_researcher',
    description="Досліджує мобільні технології",
    instruction="Опиши тренди у мобільній розробці."
)

# 🔹 Parallel агент
root_agent = ParallelAgent(
    name="research_team",
    description="Паралельне дослідження технологій",
    agents=[ai_researcher, web_researcher, mobile_researcher],
)