# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: ReadingCircle
def export_state():
    import json
    from collections import OrderedDict
    
    # Собираем все данные из глобальных словарей проекта (предполагается, что они называются data_participants, data_books и т.д.)
    # Если структура данных отличается, нужно адаптировать этот блок под конкретные имена переменных.
    
    state = {
        "participants": list(data_participants.items()),
        "books": list(data_books.items()),
        "meetings": list(data_meetings.items()),
        "questions": list(data_questions.items()),
        "notes": list(data_notes.items())
    }
    
    # Преобразуем внутренние представления (например, списки или объекты) в простые типы для JSON
    def serialize(obj):
        if isinstance(obj, dict):
            return {k: serialize(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [serialize(item) for item in obj]
        elif hasattr(obj, '__dict__'):
            # Если объект имеет атрибуты (например, класс Participant), сериализуем его как словарь
            return {k: serialize(v) for k, v in obj.__dict__.items()}
        else:
            return str(obj) if not isinstance(obj, (str, int, float, bool)) else obj
    
    serialized_state = serialize(state)
    
    # Создаем JSON-строку с красивым форматированием или компактным, если нужно
    json_string = json.dumps(serialized_state, indent=2, ensure_ascii=False)
    
    return json_string

# Пример использования:
# state_json = export_state()
# print(state_json)
