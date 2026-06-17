# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: ReadingCircle
import json, uuid, datetime as dt

def init_app():
    db = {
        "users": [
            {"id": str(uuid.uuid4())[:8], "name": "Анна", "role": "admin"},
            {"id": str(uuid.uuid4())[:8], "name": "Иван", "role": "member"}
        ],
        "books": [
            {"title": "1984", "author": "Дж. Оруэлл", "year": 1949},
            {"title": "Мастер и Маргарита", "author": "М. Булгаков", "year": 1967}
        ],
        "meetings": [
            {"date": dt.date.today().isoformat(), "topic": "Обсуждение '1984'", "attendees": ["Анна"]}
        ],
        "questions": [{"book_id": 0, "text": "Что такое Большой Брат?"}],
        "notes": [{"user_id": db["users"][0]["id"], "content": "Первый черновик"}]
    }
    with open("reading_circle_data.json", "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    init_app()
