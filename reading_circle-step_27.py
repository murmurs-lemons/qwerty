# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: ReadingCircle
def reset_demo_data():
    """Сбрасывает все демо-данные в исходные значения."""
    global _demo_books, _demo_members, _demo_events, _demo_questions, _demo_notes, _demo_counter

    _demo_books = [
        {"title": "Мастер и Маргарита", "author": "Булгаков М.А.", "pages": 275},
        {"title": "Преступление и наказание", "author": "Достоевский Ф.М.", "pages": 460},
        {"title": "Война и мир", "author": "Толстой Л.Н.", "pages": 1225},
    ]

    _demo_members = [
        {"name": "Анна Иванова", "email": "anna@example.com", "role": "reader"},
        {"name": "Борис Петров", "email": "boris@example.com", "role": "organizer"},
        {"name": "Виктория Сидорова", "email": "vika@example.com", "role": "moderator"},
    ]

    _demo_events = [
        {"date": "2025-04-12", "topic": "Обсуждение Булгакова", "capacity": 15},
        {"date": "2025-05-20", "topic": "Встреча по Достоевскому", "capacity": 20},
    ]

    _demo_questions = [
        {"text": "Какой смысл у образа Воланда?", "author": "Анна Иванова"},
        {"text": "Зачем Раскольникову его теория?", "author": "Борис Петров"},
    ]

    _demo_notes = [
        {"text": "Мастер — гениальный писатель, преследуемый властью.", "author": "Анна Иванова"},
        {"text": "Раскольников делит людей на «тварей дрожащих» и «право имеющих».", "author": "Борис Петров"},
    ]

    _demo_counter = 100


def clear_all_data():
    """Полностью очищает все данные, возвращая коллекции в пустое состояние."""
    global _demo_books, _demo_members, _demo_events, _demo_questions, _demo_notes, _demo_counter

    _demo_books.clear()
    _demo_members.clear()
    _demo_events.clear()
    _demo_questions.clear()
    _demo_notes.clear()
    _demo_counter = 0


def print_status():
    """Выводит краткую статистику текущего состояния."""
    print(f"Книги: {_demo_counter}")
