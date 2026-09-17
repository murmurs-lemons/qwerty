# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: ReadingCircle
def demo():
    print("=== ReadingCircle Demo ===")
    
    # Создаем участников
    members = [
        Member("Анна", "anna@example.com"),
        Member("Борис", "boris@example.com"),
        Member("Виктория", "victoria@example.com"),
    ]
    
    # Создаем книги
    books = [
        Book("1984", "Джордж Оруэлл"),
        Book("Мастер и Маргарита", "Михаил Булгаков"),
        Book("Бедные люди", "Федор Достоевский"),
    ]
    
    # Создаем встречи
    meetings = [
        Meeting("Обсуждение '1984'", "2024-03-15"),
        Meeting("Встреча по 'Мастеру и Маргарите'", "2024-04-20"),
    ]
    
    # Создаем вопросы
    questions = [
        Question("Что символизирует Большой Брат?", "Анна"),
        Question("Какова роль Иешуа?", "Борис"),
    ]
    
    # Создаем заметки
    notes = [
        Note("Интересная глава о прозрении", "Анна"),
        Note("Отличный дискуссионный момент", "Борис"),
    ]
    
    # Записи в журнал
    logs = [
        Log("Система запущена", "system"),
        Log(f"Добавлено {len(members)} участников", "system"),
        Log(f"Добавлено {len(books)} книг", "system"),
        Log(f"Добавлено {len(meetings)} встреч", "system"),
        Log(f"Добавлено {len(questions)} вопросов", "system"),
        Log(f"Добавлено {len(notes)} заметок", "system"),
    ]
    
    # Выводим результаты
    print(f"Участников: {len(members)}")
    print(f"Книги: {len(books)}")
    print(f"Встречи: {len(meetings)}")
    print(f"Вопросы: {len(questions)}")
    print(f"Заметки: {len(notes)}")
    print(f"Записей в журнале: {len(logs)}")
    
    print("\nДемо успешно завершено!")
