# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: ReadingCircle
import json, os

DATA_FILE = "data.json"
VERSION = 46

def migrate_data():
    if not os.path.exists(DATA_FILE):
        return
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    if data.get("__version__") != VERSION:
        raise RuntimeError(f"Unsupported data version: {data.get('__version__')}")
    if "members" not in data:
        data["members"] = []
    if "books" not in data:
        data["books"] = []
    if "meetings" not in data:
        data["meetings"] = []
    if "questions" not in data:
        data["questions"] = []
    if "notes" not in data:
        data["notes"] = []
    data["__version__"] = VERSION
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
