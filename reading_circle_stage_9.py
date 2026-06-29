# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: ReadingCircle
import json, uuid
INITIAL_DATA = '''{
    "users": [
        {"id": 1, "name": "Анна", "email": "anna@example.com"},
        {"id": 2, "name": "Борис", "email": "boris@example.com"}
    ],
    "books": [
        {"id": 101, "title": "Мастер и Маргарита", "author": "Булгаков"},
        {"id": 102, "title": "Преступление и наказание", "author": "Достоевский"}
    ],
    "meetings": [
        {"id": 501, "book_id": 101, "date": "2024-11-15T18:30:00Z"},
        {"id": 502, "book_id": 102, "date": "2024-11-22T19:00:00Z"}
    ],
    "questions": [
        {"id": 301, "meeting_id": 501, "text": "Как вы оцениваете роль Воланда?", "author_id": 1},
        {"id": 302, "meeting_id": 501, "text": "Почему Мастер не смог найти любовь?", "author_id": 2}
    ],
    "notes": [
        {"id": 401, "meeting_id": 501, "content": "Обсудили символику кошмара.", "author_id": 1},
        {"id": 402, "meeting_id": 502, "content": "Споры о финале романа.", "author_id": 2}
    ]
}'''

def load_initial_data():
    try:
        data = json.loads(INITIAL_DATA)
        # Генерируем уникальные ID для новых записей при импорте, если нужно расширить логику
        for item in data.get("users", []):
            if not item.get("_internal_id"):
                item["_internal_id"] = str(uuid.uuid4())[:8]
        return data
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга начальных данных: {e}")
        return None

# Инициализация базы данных из JSON-строки
initial_db_state = load_initial_data()
