# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: ReadingCircle
def check_overdue_reminders():
    now = datetime.now()
    overdue = []
    for reminder in reminders:
        if is_expired(reminder, now):
            overdue.append(reminder)
    return overdue
