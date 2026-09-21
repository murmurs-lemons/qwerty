# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: ReadingCircle
import json
from datetime import datetime

def sanitize_title(title: str) -> str:
    return ' '.join(title.split())[:80]

def format_message(sender: str, content: str, ts: datetime = None) -> str:
    ts_str = ts.strftime('%Y-%m-%d %H:%M') if ts else datetime.now().strftime('%Y-%m-%d %H:%M')
    return f"[{ts_str}] {sender}: {content}"

def build_question_card(books: list, author: str, question: str) -> dict:
    return {
        'books': books,
        'author': sanitize_title(author),
        'question': question,
        'votes': 0,
        'comments': [],
        'created_at': datetime.now().isoformat()
    }

def build_note(author: str, text: str, tags: list = None) -> dict:
    return {
        'author': sanitize_title(author),
        'text': text,
        'tags': tags or [],
        'created_at': datetime.now().isoformat()
    }

def build_event_card(title: str, date: datetime, location: str, description: str = '') -> dict:
    return {
        'title': sanitize_title(title),
        'date': date.isoformat(),
        'location': location,
        'description': description,
        'attendees': []
    }
