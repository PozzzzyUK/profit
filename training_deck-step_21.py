# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: TrainingDeck
import datetime

class Reminder:
    def __init__(self, topic_name, due_date):
        self.topic_name = topic_name
        self.due_date = due_date

    def is_overdue(self):
        return datetime.date.today() > self.due_date

    def display_reminder(self):
        status = "⏰" if not self.is_overdue() else "🔴"
        return f"{status} {self.topic_name}: до {self.due_date.isoformat()}"


def manage_reminders(reminders, due_date_str=None):
    new_due = datetime.date.today().replace(day=20) if due_date_str is None else datetime.date.fromisoformat(due_date_str)
    reminders.append(Reminder("Матрицы", new_due))
    print(f"Добавлено напоминание: {reminders[-1].display_reminder()}")


if __name__ == "__main__":
    manage_reminders([], "2025-03-20")
