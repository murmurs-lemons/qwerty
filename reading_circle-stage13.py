# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: ReadingCircle
def search_entities(entities, query):
    if not query:
        return entities
    q = query.lower().strip()
    results = []
    for e in entities:
        searchable_fields = [e.get('name', ''), e.get('author', '')] + \
                            list(e.get('tags', [])).split(',') + \
                            (list(e.get('content', '').split()) if isinstance(e.get('content'), str) else [])
        if any(q in field.lower() for field in searchable_fields):
            results.append(e)
    return results
