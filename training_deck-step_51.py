# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: TrainingDeck
from datetime import datetime

class ChangeLog:
    def __init__(self):
        self.entries = []

    def log(self, action, details, user="system"):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "details": details,
            "user": user
        }
        self.entries.append(entry)

    def get_history(self):
        return self.entries
