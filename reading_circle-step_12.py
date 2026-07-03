# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: ReadingCircle
def load_from_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Загружено {len(data)} записей из '{file_path}'")
        return data
    except FileNotFoundError:
        print(f"Ошибка: файл '{file_path}' не найден.")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON в файле '{file_path}': {e}")
        return []
