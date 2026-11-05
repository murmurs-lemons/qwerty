# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: ReadingCircle
def parse_text_records(path):
    records = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split('\t')
            if len(parts) != 5:
                continue
            try:
                value = int(parts[4])
            except ValueError:
                continue
            records.append({
                'type': parts[0],
                'id': parts[1],
                'name': parts[2],
                'detail': parts[3],
                'value': value,
            })
    return records
