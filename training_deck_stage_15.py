# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: TrainingDeck
def weekly_stats(records):
    if not records:
        return {}
    
    from collections import defaultdict
    
    stats = defaultdict(int)
    
    for record in records:
        date_str = record.get('date', '')
        if not date_str:
            continue
        
        try:
            week_num, _, _ = date_str.split('-')
            stats[week_num] += 1
        except (ValueError, AttributeError):
            pass
    
    return dict(sorted(stats.items()))
