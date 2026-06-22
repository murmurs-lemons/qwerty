# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: ReadingCircle
def edit_record(record_id, field_name, new_value):
    if record_id not in records:
        print(f"Запись с ID {record_id} не найдена.")
        return False
    
    try:
        index = next(i for i, r in enumerate(records) if r['id'] == record_id)
        field_map = {'name': 'title', 'author': 'author', 'date': 'date'}
        key = field_map.get(field_name.lower(), field_name)
        
        if not isinstance(new_value, str):
            new_value = str(new_value).strip()
            
        records[index][key] = new_value
        
        print(f"Запись {record_id} успешно обновлена.")
        return True
    except Exception as e:
        print(f"Ошибка при редактировании: {e}")
        return False
