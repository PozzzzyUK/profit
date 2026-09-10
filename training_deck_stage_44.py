# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: TrainingDeck
def backup_data_file(filepath, backup_dir="backups"):
    """Создаёт резервную копию файла данных с текущей меткой времени."""
    import os, shutil
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Файл {filepath} не существует")
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"backup_{os.path.basename(filepath)}_{timestamp}")
    shutil.copy2(filepath, backup_path)
    return backup_path
