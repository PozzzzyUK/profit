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
