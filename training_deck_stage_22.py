# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: TrainingDeck
def check_expired_reminders():
    """Return list of reminder ids that are past their scheduled time."""
    now = datetime.datetime.now(datetime.timezone.utc)
    expired = []
    for r in reminders:
        if isinstance(r, Reminder):
            if r.scheduled_time <= now and not r.fired_at:
                expired.append(r.id)
    return expired

def fire_pending_reminders():
    """Mark all currently-expiring reminders as fired."""
    now = datetime.datetime.now(datetime.timezone.utc)
    for r in reminders:
        if isinstance(r, Reminder):
            if r.scheduled_time <= now and not r.fired_at:
                r.fired_at = now
