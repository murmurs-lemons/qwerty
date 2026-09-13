# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: ReadingCircle
def backup_data():
    """Создаёт резервную копию файла данных в формате JSON."""
    import json, os, datetime
    data_file = 'data.json'
    if not os.path.exists(data_file):
        return
    backup_dir = 'backups'
    os.makedirs(backup_dir, exist_ok=True)
    ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = os.path.join(backup_dir, f'data_{ts}.json')
    with open(data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    with open(backup_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'Резервная копия сохранена: {backup_path}')
