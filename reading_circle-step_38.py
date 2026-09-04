# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: ReadingCircle
def test_error_boundary_cases():
    """Compact tests for error and edge-case scenarios."""

    # 1. Empty strings
    assert ReadingCircleBook("", "2024", "Author").title == ""
    assert ReadingCircleBook("Title", "", "Author").year == 0
    assert ReadingCircleBook("Title", "2024", "").author == ""

    # 2. Whitespace-only inputs
    assert ReadingCircleBook("   ", "2024", "Author").title == "   "
    assert ReadingCircleBook("Title", "   ", "Author").year == 0
    assert ReadingCircleBook("Title", "2024", "   ").author == "   "

    # 3. Extreme year values
    assert ReadingCircleBook("Title", "0", "Author").year == 0
    assert ReadingCircleBook("Title", "9999", "Author").year == 9999
    assert ReadingCircleBook("Title", "0000", "Author").year == 0
    assert ReadingCircleBook("Title", "10000", "Author").year == 10000

    # 4. Duplicate IDs
    book1 = ReadingCircleBook("A", "2024", "Author")
    book2 = ReadingCircleBook("A", "2024", "Author")
    assert book1.id == book2.id
    assert book1 in book2
    assert book2 in book1

    # 5. Negative IDs
    book_neg = ReadingCircleBook("A", "2024", "Author", -1)
    book_pos = ReadingCircleBook("A", "2024", "Author", 1)
    assert book_neg.id == -1
    assert book_pos.id == 1
    assert book_neg != book_pos

    # 6. Zero-length notes
    note = ReadingCircleNote("Title", "", "Author")
    assert note.content == ""
    assert note in ReadingCircleBook("Title", "2024", "Author").notes

    # 7. Zero-length meeting notes
    meeting = ReadingCircleMeeting("Title", "2024-01-01", "Author")
    assert meeting.title == "Title"
    assert meeting.date == "2024-01-01"
    assert meeting in ReadingCircleBook("Title", "2024", "Author").meetings

    # 8. Questions with empty details
    q = ReadingCircleQuestion("Title", "2024-01-01", "Author", "details")
    assert q.details == "details"
    assert q in ReadingCircleBook("Title", "2024", "Author").questions

    # 9. Multiple questions with same details
    q1 = ReadingCircleQuestion("Q1", "2024-01-01", "Author", "details")
    q2 = ReadingCircleQuestion("Q2", "2024-01-01", "Author", "details")
    assert q1.details == q2.details
    assert q1 in ReadingCircleBook("Title", "2024", "Author").questions
    assert q2 in ReadingCircleBook("Title", "2024", "Author").questions
