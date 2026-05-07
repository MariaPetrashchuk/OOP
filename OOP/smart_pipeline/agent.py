from google.adk.agents.llm_agent import Agent
from google.adk.agents.workflow.parallel_agent import ParallelAgent
from google.adk.agents.workflow.sequential_agent import SequentialAgent
from google.adk.agents.workflow.loop_agent import LoopAgent

# =========================
# 🔹 PARALLEL (збір даних)
# =========================

ai_agent = Agent(
    model='gemini-2.5-flash',
    name='ai_agent',
    instruction="Збери інформацію про тренди в AI."
)

web_agent = Agent(
    model='gemini-2.5-flash',
    name='web_agent',
    instruction="Збери інформацію про тренди у веб-розробці."
)

mobile_agent = Agent(
    model='gemini-2.5-flash',
    name='mobile_agent',
    instruction="Збери інформацію про тренди у мобільній розробці."
)

parallel_stage = ParallelAgent(
    name="data_collection",
    agents=[ai_agent, web_agent, mobile_agent],
)

# =========================
# 🔹 SEQUENTIAL (обробка)
# =========================

processor = Agent(
    model='gemini-2.5-flash',
    name='processor',
    instruction="Об'єднай отриману інформацію в один текст."
)

analyzer = Agent(
    model='gemini-2.5-flash',
    name='analyzer',
    instruction="Проаналізуй текст та виділи головні ідеї."
)

reporter = Agent(
    model='gemini-2.5-flash',
    name='reporter',
    instruction="Сформуй короткий звіт."
)

sequential_stage = SequentialAgent(
    name="processing_pipeline",
    agents=[processor, analyzer, reporter],
)

# =========================
# 🔹 LOOP (покращення)
# =========================

improver = Agent(
    model='gemini-2.5-flash',
    name='improver',
    instruction="Покращ текст: зроби його чіткішим і красивішим."
)

def exit_loop(context):
    return context.iteration >= 2

loop_stage = LoopAgent(
    name="improvement_loop",
    agents=[improver],
    exit_condition=exit_loop,
)

# =========================
# 🔹 ГОЛОВНИЙ PIPELINE
# =========================

root_agent = SequentialAgent(
    name="smart_pipeline",
    description="Комбінований агент: parallel + sequential + loop",
    agents=[parallel_stage, sequential_stage, loop_stage],
)