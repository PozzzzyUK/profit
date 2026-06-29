# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: TrainingDeck
def export_state():
    import json
    state = {
        "topics": list(topics.values()),
        "progress": progress,
        "settings": settings
    }
    return json.dumps(state, ensure_ascii=False, indent=2)
