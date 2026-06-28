# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: ReadingCircle
def show_menu():
    print("\n=== Меню ReadingCircle ===")
    print("1. Список участников")
    print("2. Список книг")
    print("3. Ближайшие встречи")
    print("4. Новые вопросы")
    print("5. Мои заметки")
    print("0. Выход")

def handle_command(cmd):
    if cmd == "1":
        for u in participants:
            print(f"- {u['name']} ({u['role']})")
    elif cmd == "2":
        for b in books:
            print(f"- {b['title']} (Автор: {b['author']}, Статус: {b['status']})")
    elif cmd == "3":
        if not meetings:
            print("Встречи пока не запланированы.")
        else:
            for m in sorted(meetings, key=lambda x: x['date']):
                print(f"- {m['title']} ({m['date']})")
    elif cmd == "4":
        if not questions:
            print("Новых вопросов нет.")
        else:
            for q in questions:
                print(f"- [{q['author']}] {q['text']}")
    elif cmd == "5":
        if user_notes is None or len(user_notes) == 0:
            print("У вас пока нет заметок.")
        else:
            for i, note in enumerate(user_notes):
                print(f"{i+1}. {note}")
    elif cmd == "0":
        return True
    return False

def run_cli():
    while True:
        show_menu()
        try:
            choice = input("Ваш выбор (0-5): ").strip()
            if handle_command(choice):
                break
        except KeyboardInterrupt:
            print("\nВыход из программы.")
            break
