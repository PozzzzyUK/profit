# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: TrainingDeck
import json, os

DATA_FILE = "training_deck_data.json"

def save_state(data):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"[Error] Failed to save data: {e}")
        return False

def load_state():
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {}
