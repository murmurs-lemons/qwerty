# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: ReadingCircle
import unittest

class TestReadingCircle(unittest.TestCase):
    def test_create_participant(self):
        from reading_circle import Participant
        p = Participant("Анна", 25)
        self.assertEqual(p.name, "Анна")
        self.assertEqual(p.age, 25)

    def test_create_book(self):
        from reading_circle import Book
        b = Book("Улисс", "Джойс")
        self.assertEqual(b.title, "Улисс")
        self.assertEqual(b.author, "Джойс")

    def test_create_meeting(self):
        from reading_circle import Meeting
        m = Meeting("Обсуждение Улисса", "2025-11-10")
        self.assertEqual(m.topic, "Обсуждение Улисса")
        self.assertEqual(m.date, "2025-11-10")

    def test_create_question(self):
        from reading_circle import Question
        q = Question("Что такое поток сознания?", "Анна", "Улисс")
        self.assertEqual(q.text, "Что такое поток сознания?")
        self.assertEqual(q.author, "Анна")
        self.assertEqual(q.book_title, "Улисс")

    def test_create_note(self):
        from reading_circle import Note
        n = Note("Мне понравилось начало", "Анна", "Улисс")
        self.assertEqual(n.text, "Мне понравилось начало")
        self.assertEqual(n.author, "Анна")
        self.assertEqual(n.book_title, "Улисс")

    def test_participant_add_book(self):
        from reading_circle import Participant
        p = Participant("Борис", 30)
        book = Book("Мастер и Маргарита", "Булгаков")
        p.add_book(book)
        self.assertEqual(len(p.books), 1)
        self.assertEqual(p.books[0].title, "Мастер и Маргарита")

    def test_participant_add_question(self):
        from reading_circle import Participant
        p = Participant("Виктор", 28)
        q = Question("Хорошая ли книга?", "Виктор", "Мастер и Маргарита")
        p.add_question(q)
        self.assertEqual(len(p.questions), 1)

    def test_participant_add_note(self):
        from reading_circle import Participant
        p = Participant("Елена", 35)
        n = Note("Книга глубокaя", "Елена", "Мастер и Маргарита")
        p.add_note(n)
        self.assertEqual(len(p.notes), 1)

    def test_participant_add_meeting(self):
        from reading_circle import Participant
        p = Participant("Дмитрий", 40)
        m = Meeting("Обсуждение Булгакова", "2025-12-01")
        p.add_meeting(m)
        self.assertEqual(len(p.meetings), 1)

    def test_participant_get_books(self):
        from reading_circle import Participant
        p = Participant("Сергей", 33)
        b1 = Book("Война и мир", "Толстой")
        b2 = Book("Мастер и Маргарита", "Булгаков")
        p.add_book(b1)
        p.add_book(b2)
        books = p.get_books()
        self.assertEqual(len(books), 2)

    def test_participant_get_questions(self):
        from reading_circle import Participant
        p = Participant("Ольга", 27)
        q1 = Question("Сильная ли книга?", "Ольга", "Война и мир")
        q2 = Question("Что думать о финале?", "Ольга", "Война и мир")
        p.add_question(q1)
        p.add_question(q2)
        questions = p.get_questions()
        self.assertEqual(len(questions), 2)

    def test_participant_get_notes(self):
        from reading_circle import Participant
        p = Participant("Павел", 38)
        n1 = Note("Интересно", "Павел", "Война и мир")
        n2 = Note("Грустно", "Павел", "Война и мир")
        p.add_note(n1)
        p.add_note(n2)
        notes = p.get_notes()
        self.assertEqual(len(notes), 2)

    def test_participant_get_meetings(self):
        from reading_circle import Participant
        p = Participant("Наталья", 31)
        m1 = Meeting("Обсуждение Толстого", "2025-10-15")
        m2 = Meeting("Обсуждение Булгакова", "2025-11-20")
        p.add_meeting(m1)
        p.add_meeting(m2)
        meetings = p.get_meetings()
        self.assertEqual(len(meetings), 2)

    def test_participant_total_count(self):
        from reading_circle import Participant
        p = Participant("Иван", 45)
        b = Book("Тихий Дон", "Шолохов")
        q = Question("Как герой?", "Иван", "Тихий Дон")
        n = Note("Эпично", "Иван", "Тихий Дон")
        m = Meeting("Обсуждение Шолохова", "2025-12-05")
        p.add_book(b)
        p.add_question(q)
        p.add_note(n)
        p.add_meeting(m)
        self.assertEqual(p.total_count, 4)

if __name__ == '__main__':
    unittest.main()
