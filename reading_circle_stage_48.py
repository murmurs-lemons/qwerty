# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: ReadingCircle
def _find_or_create_event(event_id: str) -> Event:
    """Найти событие по ID или создать новое."""
    for e in events:
        if e.id == event_id:
            return e
    return Event(id=event_id)

def _find_or_create_note(note_id: str) -> Note:
    """Найти заметку по ID или создать новую."""
    for n in notes:
        if n.id == note_id:
            return n
    return Note(id=note_id)

def _find_or_create_question(question_id: str) -> Question:
    """Найти вопрос по ID или создать новый."""
    for q in questions:
        if q.id == question_id:
            return q
    return Question(id=question_id)
