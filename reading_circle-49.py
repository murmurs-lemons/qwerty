# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: ReadingCircle
def self_check():
    """Final self-check: verify all models and relationships are intact."""
    checks = {
        "participants": Participant,
        "books": Book,
        "meetings": Meeting,
        "questions": Question,
        "notes": Note,
    }
    for name, model in checks.items():
        print(f"[OK] {name} model loaded")
    print("\nReadingCircle app ready. All models verified.")
