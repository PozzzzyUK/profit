# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: TrainingDeck
import json, os

def load_training_data(file_path: str) -> dict | None:
    if not file_path or not os.path.exists(file_path):
        print(f"Ошибка: файл '{file_path}' не найден.")
        return None
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, dict) and "topics" in data:
            print(f"Успешно загружено {len(data['topics'])} тем из '{file_path}'.")
            return data
        else:
            print("Ошибка: некорректная структура JSON (отсутствует ключ 'topics').")
            return None
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON в файле '{file_path}': {e}")
        return None
    except PermissionError:
        print(f"Ошибка доступа к файлу '{file_path}'. Проверьте права.")
        return None
