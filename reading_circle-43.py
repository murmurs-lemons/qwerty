# === Stage 43: Добавь пагинацию длинных списков ===
# Project: ReadingCircle
def paginate(items, page_size=10, current_page=1):
    """Compact paginator for long lists."""
    total_pages = max(1, (len(items) + page_size - 1) // page_size)
    if current_page < 1 or current_page > total_pages:
        current_page = 1
    start = (current_page - 1) * page_size
    end = start + page_size
    page = items[start:end]
    return {
        'data': page,
        'page': current_page,
        'total_pages': total_pages,
        'total': len(items),
        'page_size': page_size,
    }
