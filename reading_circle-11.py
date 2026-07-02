# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: ReadingCircle
import json, os

DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"participants": [], "books": [], "meetings": [], "questions": [], "notes": []}
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {"participants": [], "books": [], "meetings": [], "questions": [], "notes": []}

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
