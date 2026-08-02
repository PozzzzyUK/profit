# === Stage 32: Добавь журнал действий пользователя ===
# Project: TrainingDeck
class ActionLog:
    def __init__(self):
        self.entries = []

    def log(self, action_type: str, details: dict):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action_type": action_type,
            **details
        }
        self.entries.append(entry)

    def get_summary(self) -> list:
        return [entry for entry in self.entries if entry["action_type"] == "completed"]

    def get_recent(self, n: int = 5) -> list:
        return self.entries[-n:]
