# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: TrainingDeck
def parse_date(date_str):
    """Парсинг даты в формате 'YYYY-MM-DD'. Возвращает datetime.date или строку с ошибкой."""
    import re
    from datetime import date
    pattern = r'^(\d{4})-(\d{2})-(\d{2})$'
    m = re.match(pattern, date_str)
    if not m:
        return f"Ошибка: некорректный формат даты '{date_str}'. Ожидается YYYY-MM-DD."
    y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
    try:
        return date(y, mo, d)
    except ValueError as e:
        return f"Ошибка: некорректная дата '{date_str}'. {e}"
