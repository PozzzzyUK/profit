# === Stage 20: Добавь восстановление записей из архива ===
# Project: TrainingDeck
def recover_from_archive(archive_path, deck):
    if not os.path.exists(archive_path):
        print("Archive file not found.")
        return False
    with open(archive_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for entry in data.get('records', []):
        deck.add_record(entry['topic'], entry['exercise'], entry.get('check', ''), entry.get('progress', {}))
    print(f"Recovered {len(data.get('records', []))} records from archive.")
    return True
