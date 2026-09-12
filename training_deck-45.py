# === Stage 45: Добавь восстановление из резервной копии ===
# Project: TrainingDeck
import json, copy

def load_backup(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_backup(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def restore_from_backup(source_path, target_path):
    backup_data = load_backup(source_path)
    with open(target_path, 'r', encoding='utf-8') as f:
        current = json.load(f)
    deep_copy = copy.deepcopy(backup_data)
    with open(target_path, 'w', encoding='utf-8') as f:
        json.dump(deep_copy, f, ensure_ascii=False, indent=2)
    print(f"Восстановлено из {source_path} -> {target_path}")
