# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: ReadingCircle
def export_report():
    print("Отчёт по клубу чтения")
    print("=" * 30)
    print(f"Участников: {len(participants)}")
    print(f"Книг: {len(books)}")
    print(f"Встреч: {len(meetings)}")
    print(f"Вопросов: {len(questions)}")
    print(f"Заметок: {len(notes)}")
    with open("report.txt", "w") as f:
        f.write("Отчёт по клубу чтения\n")
        f.write("=" * 30 + "\n")
        f.write(f"Участников: {len(participants)}\n")
        f.write(f"Книг: {len(books)}\n")
        f.write(f"Встреч: {len(meetings)}\n")
        f.write(f"Вопросов: {len(questions)}\n")
        f.write(f"Заметок: {len(notes)}\n")
