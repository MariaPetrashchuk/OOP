import logging
from google.adk.agents.llm_agent import Agent
import datetime

# Логування
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Інструмент часу
def get_current_time(city: str) -> dict:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    logger.info(f"Отримання часу для міста: {city}")
    return {
        "status": "success",
        "city": city,
        "time": current_time
    }

# Інструмент логування
def logging_tool(param: str) -> dict:
    logger.info(f"Виклик logging_tool з параметром: {param}")
    return {"result": "success", "processed_param": param}

# ОДИН агент
root_agent = Agent(
    model='gemini-2.5-flash',
    name='time_logging_agent',
    description="Агент з визначення часу та логуванням.",
    instruction="Використовуй get_current_time для часу і logging_tool для логування.",
    tools=[get_current_time, logging_tool],
)