# === Stage 55: Добавь мягкую проверку дубликатов при создании записей ===
# Project: ReadingCircle
def _safe_unique_key(store, key_field):
    try:
        return store.get(key_field)
    except Exception:
        return None

def _find_duplicate(store, record, key_field):
    key = _safe_unique_key(record, key_field)
    if key is None:
        return None
    for existing in store.values():
        if existing is record:
            continue
        if _safe_unique_key(existing, key_field) == key:
            return existing
    return None

def _apply_duplicate_policy(store, record, policy, key_field):
    duplicate = _find_duplicate(store, record, key_field)
    if duplicate is None:
        return False
    if policy == "allow":
        return False
    if policy == "update":
        for field in record:
            if field != key_field:
                setattr(duplicate, field, getattr(record, field))
        return False
    if policy == "skip":
        return False
    return False
