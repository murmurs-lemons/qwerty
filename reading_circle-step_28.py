# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: ReadingCircle
import statistics

def project_metrics(circles, books, members):
    active_circles = [c for c in circles if len(c.get('meetings', [])) > 0]
    total_meetings = sum(len(c['meetings']) for c in circles)
    avg_participants_per_circle = statistics.mean([len(c['members']) for c in circles]) if circles else 0.0
    unique_authors = set()
    most_popular_book = None
    max_book_reads = 0
    total_questions = sum(len(b.get('questions', [])) for b in books)
    active_members_count = len(members)

    return {
        'total_circles': len(circles),
        'active_circles': len(active_circles),
        'total_meetings_held': total_meetings,
        'avg_participants_per_circle': round(avg_participants_per_circle, 1),
        'unique_authors_count': len(unique_authors),
        'most_popular_book': most_popular_book,
        'max_reads_of_most_popular': max_book_reads,
        'total_questions_asked': total_questions,
        'active_members': active_members_count,
    }
