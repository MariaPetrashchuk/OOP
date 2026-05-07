from google.adk.agents.llm_agent import Agent

# 🔹 Інструмент: безпечне ділення
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
        return {"error": "Ділення на нуль неможливе", "result": None}
    return {"result": a / b, "error": None}


# 🔹 Інструмент: підрахунок слів
def count_words(text: str) -> dict:
    """
    Підраховує кількість слів у тексті.

    Args:
        text: вхідний текст

    Returns:
        dict: статистика
    """
    if not text.strip():
        return {"error": "Текст порожній", "count": 0}

    words = text.split()
    return {
        "count": len(words),
        "unique": len(set(words)),
        "error": None
    }


# 🔹 Агент
root_agent = Agent(
    model='gemini-2.5-flash',
    name='smart_helper',
    description="Агент для обчислень та аналізу тексту",
    instruction="""
    Ти розумний помічник.

    Твої задачі:
    - допомагати з математикою
    - аналізувати текст
    - перевіряти помилки

    Використовуй доступні інструменти.
    Відповідай українською мовою.
    Пояснюй результат просто і зрозуміло.
    """,
    tools=[safe_divide, count_words],
)