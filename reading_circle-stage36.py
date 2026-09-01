# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: ReadingCircle
def check_integrity():
    """Проверяет целостность данных: участники, книги, встречи, вопросы, заметки."""
    errors = []
    if not participants:
        errors.append("Участники отсутствуют")
    for p in participants:
        if not p.get("id"):
            errors.append(f"Участник без ID: {p}")
    if not books:
        errors.append("Книги отсутствуют")
    for b in books:
        if not b.get("id") or not b.get("title"):
            errors.append(f"Книга без ID или названия: {b}")
    if not meetings:
        errors.append("Встречи отсутствуют")
    for m in meetings:
        if not m.get("id") or not m.get("book_id"):
            errors.append(f"Встреча без ID или book_id: {m}")
    if not questions:
        errors.append("Вопросы отсутствуют")
    for q in questions:
        if not q.get("id") or not q.get("book_id"):
            errors.append(f"Вопрос без ID или book_id: {q}")
    if not notes:
        errors.append("Заметки отсутствуют")
    for n in notes:
        if not n.get("id") or not n.get("book_id"):
            errors.append(f"Заметка без ID или book_id: {n}")
    return errors


def repair_simple_issues():
    """Ремонтирует простые проблемы: добавляет ID, если они отсутствуют."""
    if not participants:
        participants = []
    for i, p in enumerate(participants):
        if "id" not in p:
            p["id"] = str(i + 1)
    if not books:
        books = []
    for i, b in enumerate(books):
        if "id" not in b:
            b["id"] = str(i + 1)
    if not meetings:
        meetings = []
    for i, m in enumerate(meetings):
        if "id" not in m:
            m["id"] = str(i + 1)
    if not questions:
        questions = []
    for i, q in enumerate(questions):
        if "id" not in q:
            q["id"] = str(i + 1)
    if not notes:
        notes = []
    for i, n in enumerate(notes):
        if "id" not in n:
            n["id"] = str(i + 1)
