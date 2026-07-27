# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: TrainingDeck
def project_metrics():
    """Compute key metrics for the TrainingDeck project."""
    total_topics = len(topics) if topics else 0
    total_exercises = sum(len(ex.get("exercises", [])) for ex in exercises)
    completed_exercises = sum(1 for ex in exercises for e in ex["exercises"] if e["status"] == "completed")
    success_rate = (completed_exercises / total_exercises * 100) if total_exercises else 0.0
    avg_progress_per_topic = sum((sum(1 for e in ex["exercises"] if e["status"] == "completed") / len(ex.get("exercises", [])) * 100) 
                                 for ex in exercises if ex.get("exercises")) / total_topics if total_topics else 0.0
    return {
        "total_topics": total_topics,
        "total_exercises": total_exercises,
        "completed_exercises": completed_exercises,
        "success_rate": round(success_rate, 2),
        "avg_progress_per_topic": round(avg_progress_per_topic, 2)
    }

metrics = project_metrics()
print(f"Project Metrics: {metrics}")
