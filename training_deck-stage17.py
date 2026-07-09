# === Stage 17: Добавь группировку записей по категориям ===
# Project: TrainingDeck
def group_by_category(self, records):
        """Группирует записи по полю category."""
        groups = {}
        for rec in records:
            cat = rec.get("category", "Uncategorized")
            groups.setdefault(cat, []).append(rec)
        return dict(sorted(groups.items()))
