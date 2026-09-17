# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: TrainingDeck
class TrainingDeck:
    def __init__(self, name, topics):
        self.name = name
        self.topics = topics  # list of Topic objects
        self.progress = {}  # {topic_id: score}
        self.completed = []

    def add_topic(self, topic):
        self.topics.append(topic)
        return topic

    def get_topic(self, topic_id):
        for t in self.topics:
            if t.id == topic_id:
                return t
        return None

    def get_progress(self, topic_id):
        topic = self.get_topic(topic_id)
        if not topic:
            return 0
        return self.progress.get(topic_id, 0)

    def complete_topic(self, topic_id):
        topic = self.get_topic(topic_id)
        if topic:
            score = topic.check_progress()
            self.progress[topic_id] = score
            self.completed.append(topic_id)
            return score
        return 0

    def get_all_topics(self):
        return self.topics

    def get_stats(self):
        total = len(self.topics)
        done = len(self.completed)
        avg = sum(self.progress.values()) / total if total else 0
        return {"total": total, "done": done, "avg_score": avg}

    def show_progress(self):
        stats = self.get_stats()
        print(f"TrainingDeck: {self.name}")
        print(f"Topics: {stats['total']}, Completed: {stats['done']}/{stats['total']}")
        print(f"Average score: {stats['avg_score']:.1f}")
