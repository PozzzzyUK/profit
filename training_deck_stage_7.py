# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: TrainingDeck
def sort_records(records, key='date', reverse=False):
    if not records: return []
    def get_sort_key(r):
        val = r.get(key)
        if isinstance(val, str):
            try: int(val); return (0, val)
            except ValueError: return (1, val.lower())
        elif key == 'priority':
            p_map = {'high': 3, 'medium': 2, 'low': 1}
            return (-p_map.get(val.lower(), 0), r.get('name', ''))
        else:
            try: return (int(val) if val.isdigit() else float(val), r.get('name', ''))
            except ValueError: return (val, '')
    return sorted(records, key=get_sort_key, reverse=reverse)
