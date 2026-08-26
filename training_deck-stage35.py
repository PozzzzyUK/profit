# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: TrainingDeck
class TrainingDeck:
    def __init__(self):
        self.topics = []
        self.exercises = []
        self.checks = []
        self.progress = {}

    def add_topic(self, name, description):
        self.topics.append({"name": name, "description": description})

    def add_exercise(self, topic_name, name, difficulty, code):
        self.exercises.append({"topic": topic_name, "name": name, "difficulty": difficulty, "code": code})

    def add_check(self, topic_name, name, expected_output):
        self.checks.append({"topic": topic_name, "name": name, "expected_output": expected_output})

    def get_next_action(self):
        if not self.topics:
            return "Начни с добавления первой темы."
        if not self.exercises:
            return "Добавь упражнения для первой темы."
        if not self.checks:
            return "Добавь проверки для первой темы."
        if not self.progress:
            return "Начни отслеживать прогресс."
        return "Проект готов к демонстрации!"

    def show_status(self):
        print(f"Темы: {len(self.topics)}")
        print(f"Упражнения: {len(self.exercises)}")
        print(f"Проверки: {len(self.checks)}")
        print(f"Следующее действие: {self.get_next_action()}")

    def run(self):
        self.add_topic("Математика", "Базовые операции")
        self.add_exercise("Математика", "Сложение", "easy", "print(2+2)")
        self.add_check("Математика", "Сложение", "4")
        self.show_status()

    def run(self):
        self.add_topic("Математика", "Базовые операции")
        self.add_exercise("Математика", "Сложение", "easy", "print(2+2)")
        self.add_check("Математика", "Сложение", "4")
        self.show_status()
