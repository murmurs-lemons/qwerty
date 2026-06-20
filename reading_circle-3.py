# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: ReadingCircle
class ReadingCircle:
    def __init__(self):
        self.members = []
        self.books = []
        self.meetings = []
        self.questions = []
        self.notes = []

    def add_member(self, name, email):
        if not any(m['email'] == email for m in self.members):
            self.members.append({'name': name, 'email': email})
            return True
        return False

    def add_book(self, title, author, genre):
        self.books.append({'title': title, 'author': author, 'genre': genre})
        return len(self.books)

    def schedule_meeting(self, date, topic, organizer_id):
        self.meetings.append({
            'date': date,
            'topic': topic,
            'organizer_id': organizer_id
        })
        return len(self.meetings)

    def ask_question(self, book_title, question_text, author_name):
        self.questions.append({
            'book_title': book_title,
            'question': question_text,
            'author': author_name
        })
        return len(self.questions)

    def add_note(self, content, tags=None):
        note = {'content': content}
        if tags:
            note['tags'] = tags
        self.notes.append(note)
        return len(self.notes)
