from google.adk.agents.llm_agent import Agent

def safe_divide(a: float, b: float) -> dict:
    """
    Ділить два числа з перевіркою на нуль.

    Args:
        a: перше число
        b: друге число

    Returns:
        dict: результат або помилка
    """
    if b == 0:
        return {
            "error": "Ділення на нуль неможливе",
            "result": None
        }

    return {
        "error": None,
        "result": a / b
    }


def safe_add(a: float, b: float) -> dict:
    """
    Додає два числа.

    Args:
        a: перше число
        b: друге число

    Returns:
        dict: результат додавання
    """
    return {
        "error": None,
        "result": a + b
    }


root_agent = Agent(
    model='gemini-2.5-flash',
    name='smart_calculator',
    description="Безпечний калькулятор з перевіркою помилок.",
    
    instruction="""
    Ти точний математичний асистент.
    
    Правила:
    - Завжди використовуй доступні інструменти
    - Якщо виникає помилка — поясни її користувачу
    - Відповідай українською мовою
    - Поверни результат у зрозумілому вигляді
    
    Якщо користувач просить поділити числа — використовуй safe_divide
    Якщо додати — safe_add
    """,
    
    tools=[safe_divide, safe_add],
)