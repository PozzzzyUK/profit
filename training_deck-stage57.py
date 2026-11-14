# === Stage 57: Добавь массовое удаление с подтверждением через параметр ===
# Project: TrainingDeck
def bulk_delete(deck, ids, confirm=True):
    if confirm:
        if len(ids) != len(set(ids)):
            print("Удаление отменено: обнаружены дубликаты ID.")
            return
        ids = list(ids)
        print(f"Удалить {len(ids)} элементов из {len(deck)}? (y/n): ", end="")
        resp = input().strip().lower()
        if resp != "y":
            print("Удаление отменено.")
            return
    deck = {k: v for k, v in deck.items() if k not in ids}
    return deck
