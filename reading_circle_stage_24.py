# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: ReadingCircle
def print_record(record):
    """Компактный вывод одной записи с ключевыми полями."""
    name = getattr(record, 'name', '') or getattr(record, 'title', '')
    date = getattr(record, 'date', '') or getattr(record, 'created_at', '')
    body = getattr(record, 'body', '') or getattr(record, 'description', '')
    print(f"[{record.__class__.__name__}]")
    print(f"  Имя/название: {name}")
    print(f"  Дата:        {date}")
    if body:
        print(f"  Описание:    {body[:80]}{'...' if len(body) > 80 else ''}")
