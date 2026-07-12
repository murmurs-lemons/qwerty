# === Stage 17: Добавь группировку записей по категориям ===
# Project: ReadingCircle
def group_by_categories(records, field):
    groups = {}
    for rec in records:
        key = rec[field]
        if not isinstance(key, str):
            raise TypeError(f"Field '{field}' must be a string, got {type(key).__name__}")
        groups.setdefault(key, []).append(rec)
    return dict(sorted(groups.items()))
