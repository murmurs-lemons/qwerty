# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: ReadingCircle
def demo():
    """Демо-команды для ручного тестирования."""
    import os, sys
    p = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, p)
    from models import User, Book, Meeting, Question, Note
    u1 = User(name="Alice", email="alice@example.com")
    u2 = User(name="Bob", email="bob@example.com")
    b1 = Book(title="War and Peace", author="Tolstoy", year=1869)
    q1 = Question(text="What is the main theme?", user=u1, book=b1)
    n1 = Note(text="Great read!", user=u1, book=b1)
    m1 = Meeting(title="Book Club: War and Peace", date="2024-12-15", location="Online")
    print(f"Users: {u1}, {u2}")
    print(f"Books: {b1}")
    print(f"Questions: {q1}")
    print(f"Notes: {n1}")
    print(f"Meetings: {m1}")

demo()
