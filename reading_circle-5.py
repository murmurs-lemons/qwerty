# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: ReadingCircle
def delete_record(collection, record_id):
    if collection not in data:
        raise ValueError(f"Collection '{collection}' does not exist.")
    if record_id not in data[collection]:
        print(f"No record found with ID {record_id} in '{collection}'.")
        return False
    del data[collection][record_id]
    print(f"Record {record_id} deleted from '{collection}'.")
    return True

def handle_missing_ids(collection, id_list):
    if collection not in data:
        raise ValueError(f"Collection '{collection}' does not exist.")
    existing = set(data[collection].keys())
    missing = [i for i in id_list if str(i) not in existing]
    print(f"Missing IDs in '{collection}': {missing}")
    return list(existing & set(id_list))
