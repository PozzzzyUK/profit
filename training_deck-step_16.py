# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: TrainingDeck
def monthly_stats(self):
    """Calculate monthly statistics for all completed exercises."""
    if not self.exercises:
        return {}
    
    stats = {}
    for exercise in self.exercises:
        date_str = exercise.get("date")
        if date_str:
            month_key = f"{date_str[:7]}"  # YYYY-MM
            if month_key not in stats:
                stats[month_key] = {"total": 0, "passed": 0}
            stats[month_key]["total"] += exercise.get("attempts", [])[-1].get("result") == "success"
    
    return {k: v for k, v in stats.items() if any(v.values())}
