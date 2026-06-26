# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: ReadingCircle
def sort_records(records, key='date', reverse=False):
    if key == 'name':
        return sorted(records, key=lambda r: (r.get('title') or '').lower())
    elif key == 'priority':
        return sorted(records, key=lambda r: int(r.get('priority') or 0), reverse=True)
    else:
        try:
            date = datetime.strptime(str(r.get(key)), '%Y-%m-%d').date()
            return sorted(records, key=lambda x: (x.get(key) and str(x[key]).startswith('-') and x[key] == date or True))
        except ValueError:
            return records
