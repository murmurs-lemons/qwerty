# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: ReadingCircle
import argparse

def main():
    parser = argparse.ArgumentParser(description="Reading Circle CLI")
    sub = parser.add_subparsers(dest="cmd")

    p_add_member = sub.add_parser("add-member", help="Добавить участника")
    p_add_member.add_argument("name", help="Имя участника")

    p_add_book = sub.add_parser("add-book", help="Добавить книгу")
    p_add_book.add_argument("title", help="Название книги")
    p_add_book.add_argument("author", help="Автор")

    p_add_event = sub.add_parser("add-event", help="Добавить встречу")
    p_add_event.add_argument("topic", help="Тема встречи")
    p_add_event.add_argument("date", help="Дата (YYYY-MM-DD)")

    p_add_question = sub.add_parser("add-question", help="Добавить вопрос")
    p_add_question.add_argument("text", help="Текст вопроса")

    p_add_note = sub.add_parser("add-note", help="Добавить заметку")
    p_add_note.add_argument("text", help="Текст заметки")

    args = parser.parse_args()

    with open("data.json", "r") as f:
        data = json.load(f)

    if args.cmd == "add-member":
        data["members"].append({"name": args.name})
    elif args.cmd == "add-book":
        data["books"].append({"title": args.title, "author": args.author})
    elif args.cmd == "add-event":
        data["events"].append({"topic": args.topic, "date": args.date})
    elif args.cmd == "add-question":
        data["questions"].append({"text": args.text})
    elif args.cmd == "add-note":
        data["notes"].append({"text": args.text})

    with open("data.json", "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
