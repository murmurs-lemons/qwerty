# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: ReadingCircle
def parse_date(date_str):
    """Парсит дату в формате 'YYYY-MM-DD' или 'DD.MM.YYYY'. Возвращает datetime.date."""
    import re
    date_str = date_str.strip()
    
    # Убираем лишние пробелы и переводим всё в нижний регистр для проверки формата
    if not re.match(r'^\d{4}[-/]\d{2}[-/]\d{2}$', date_str):
        raise ValueError(f"Некорректный формат даты: {date_str}. Ожидалось YYYY-MM-DD")

    parts = date_str.split('-')
    year, month, day = int(parts[0]), int(parts[1]), int(parts[2])

    if not (1 <= month <= 12):
        raise ValueError(f"Некорректный месяц: {month}")
    
    import calendar
    max_day = calendar.monthrange(year, month)[1]
    if not (1 <= day <= max_day):
        raise ValueError(f"Некорректный день для {year}-{month}: {day} (максимум {max_day})")

    return datetime.date(year, month, day)


def format_date(date_obj):
    """Форматирует datetime.date в строку 'YYYY-MM-DD'."""
    if isinstance(date_obj, str):
        return date_obj
    return date_obj.strftime('%Y-%m-%d')
