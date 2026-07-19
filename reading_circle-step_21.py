# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: ReadingCircle
import datetime

class Reminder:
    def __init__(self, task, due_date):
        self.task = task
        self.due_date = due_date
        self.done = False

    def is_overdue(self):
        return not self.done and self.due_date < datetime.date.today()

    def check_all(self):
        overdue = [r for r in reminders if r.is_overdue()]
        if overdue:
            print(f"⚠️  Просрочены напоминания:")
            for r in overdue:
                days_left = (datetime.date.today() - r.due_date).days
                print(f"   — {r.task} (просрочено на {days_left} дн.)")


reminders = []

def add_reminder(task, due):
    reminders.append(Reminder(task, datetime.date.fromisoformat(due)))
    print(f"✅ Напоминание добавлено: '{task}' к дате {due}")

add_reminder("Прочитать главу 3", "2025-12-25")
