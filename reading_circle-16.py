# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: ReadingCircle
def monthly_stats(stats):
    """Group stats by month and return dict: YYYY-MM -> {books, events, questions, notes}."""
    grouped = {}
    for key in ('books', 'events', 'questions', 'notes'):
        items = stats.get(key, [])
        for item in items:
            date_str = item.get('date') or item.get('created_at')
            if not isinstance(date_str, str):
                continue
            try:
                year, month = map(int, date_str[:7].split('-'))
            except (ValueError, AttributeError):
                continue
            key_month = f'{year}-{month:02d}'
            grouped.setdefault(key_month, {}).setdefault(key, []).append(item)
    return grouped
