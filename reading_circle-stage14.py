# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: ReadingCircle
def generate_summary():
    """Генерирует краткую сводку по текущим данным проекта."""
    stats = {
        "participants": len(participants),
        "books": len(books),
        "meetings": len(meetings),
        "questions": len(questions),
        "notes": len(notes),
    }
    print("📊 Сводка ReadingCircle:")
    for key, value in stats.items():
        print(f"  {key}: {value}")
