# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: TrainingDeck
def delete_record(record_id, collection_name):
    if not record_id:
        raise ValueError("ID записи должен быть непустым")
    try:
        db[collection_name].pop(record_id)
        print(f"Запись с ID {record_id} удалена из коллекции '{collection_name}'.")
    except KeyError:
        print(f"Ошибка: Запись с ID {record_id} не найдена в коллекции '{collection_name}' или она уже была удалена.")

# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: TrainingDeck
def delete_record(record_id, collection_name):
    if not record_id:
        raise ValueError("ID записи должен быть непустым")
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        if collection_name not in data['collections']:
            print(f"Коллекция '{collection_name}' не найдена.")
            return False
        records = data['collections'][collection_name]
        original_count = len(records)
        for i, record in enumerate(records):
            if str(record.get('id')) == str(record_id):
                del records[i]
                print(f"Запись с ID {record_id} удалена из коллекции '{collection_name}'.")
                return True
        else:
            print(f"Запись с ID {record_id} не найдена в коллекции '{collection_name}'.")
            return False
    except json.JSONDecodeError as e:
        print(f"Ошибка чтения файла данных: {e}")
        return False
