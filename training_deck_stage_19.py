# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: TrainingDeck
def archive_records(deck, cutoff_date=None):
    """Archive completed or old records older than cutoff_date (default: 180 days ago)."""
    if not deck.get("records"):
        return deck
    now = datetime.datetime.now()
    if cutoff_date is None:
        cutoff_date = now - timedelta(days=180)
    archived_ids = []
    for record in deck["records"]:
        status = record.get("status", "active")
        created = record.get("created_at", "")
        try:
            date = datetime.datetime.fromisoformat(created) if isinstance(created, str) else created
            if date < cutoff_date and status == "completed":
                record["archived"] = True
                archived_ids.append(record["id"])
        except (ValueError, TypeError):
            pass
    deck["records"] = [r for r in deck["records"] if not (r.get("archived") or r["id"] in archived_ids)]
    return deck
