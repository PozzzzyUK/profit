# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: TrainingDeck
import json

VERSION = "0.0.1"

def migrate_structure(data, version):
    if data.get("__version__") != version:
        raise ValueError(f"Unsupported version: {data.get('__version__')}")
    return data
