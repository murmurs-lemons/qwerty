# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: ReadingCircle
from typing import Callable, Optional
def filter_records(records: list[dict], filters: dict[str, str] | None = None) -> list[dict]:
    if not filters or not records: return records
    def match(record: dict) -> bool:
        for key, value in filters.items():
            if record.get(key) != value: return False
        return True
    return [r for r in records if match(r)]

def filter_by_status(records: list[dict], status: str = "active") -> list[dict]:
    return filter_records(records, {"status": status})

def filter_by_category(records: list[dict], category: str) -> list[dict]:
    return filter_records(records, {"category": category})

def filter_by_tags(records: list[dict], tags: list[str]) -> list[dict]:
    if not tags or not records: return records
    def has_all_tags(record: dict) -> bool:
        record_tags = set(record.get("tags", []))
        required_tags = set(tags)
        return required_tags.issubset(record_tags)
    return [r for r in records if has_all_tags(r)]

def filter_by_multiple_criteria(records: list[dict], filters: dict[str, str]) -> list[dict]:
    filtered = records[:]
    for key, value in filters.items():
        filtered = filter_records(filtered, {key: value})
    return filtered
