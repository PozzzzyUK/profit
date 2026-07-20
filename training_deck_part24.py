# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: TrainingDeck
def summary_record(record):
    """Print a compact one-line summary of a training record."""
    print(f"[{record['id']}] Topic: {record.get('topic', 'N/A')} | "
          f"Exercises: {len(record.get('exercises', []))} | "
          f"Status: {record.get('status', 'unknown')}")
