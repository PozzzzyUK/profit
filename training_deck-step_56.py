# === Stage 56: Добавь массовое обновление выбранных записей ===
# Project: TrainingDeck
def bulk_update_records(deck, ids, updates):
    updated = []
    for record in deck.records:
        if record.id in ids:
            for key, value in updates.items():
                setattr(record, key, value)
            record.last_modified = datetime.now()
            updated.append(record)
    deck.save()
    return updated
