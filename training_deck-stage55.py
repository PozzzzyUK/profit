# === Stage 55: Добавь мягкую проверку дубликатов при создании записей ===
# Project: TrainingDeck
def find_duplicate_record(records, new_record):
    """Находит запись-дублёр для новой записи по ключевым полям."""
    key_fields = ["topic", "exercise", "answer"]
    for record in records:
        if all(record.get(field) == new_record.get(field) for field in key_fields):
            return record
    return None
