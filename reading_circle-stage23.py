# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: ReadingCircle
def format_table(rows, headers):
    """Форматирует список кортежей в компактную таблицу с разделителями."""
    if not rows:
        return ""
    
    # Определяем ширину каждой колонки
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(val)))
    
    # Формируем строку разделителя
    separator = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"
    
    # Строим заголовок
    header_line = "|" + "|".join(f"{h:<{col_widths[i]}}" for i, h in enumerate(headers)) + "|"
    
    # Формируем строки данных
    data_lines = []
    for row in rows:
        line = "|" + "|".join(f"{str(val):<{col_widths[i]}}" for i, val in enumerate(row)) + "|"
        data_lines.append(line)
    
    # Собираем всё вместе
    table = separator + "\n" + header_line + "\n" + separator + "\n"
    for line in data_lines:
        table += line + "\n"
    table += separator
    
    return table.strip()
