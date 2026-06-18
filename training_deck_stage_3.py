# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: TrainingDeck
class TrainingDeck:
    def __init__(self):
        self._topics = {}
        self._exercises = []
        self._progress = {}

    def add_topic(self, topic_id: str, title: str, description: str) -> None:
        if not topic_id or not title:
            raise ValueError("ID и заголовок темы обязательны")
        self._topics[topic_id] = {"title": title, "description": description}

    def add_exercise(self, exercise_id: str, topic_id: str, task: str, check_func) -> None:
        if not all([exercise_id, topic_id, task]):
            raise ValueError("ID упражнения, ID темы и задача обязательны")
        self._exercises.append({
            "id": exercise_id,
            "topic_id": topic_id,
            "task": task,
            "check_func": check_func,
            "status": "pending"
        })

    def record_progress(self, exercise_id: str, result: bool) -> None:
        for ex in self._exercises:
            if ex["id"] == exercise_id:
                ex["status"] = "completed" if result else "failed"
                break
