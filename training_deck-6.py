# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: TrainingDeck
def filter_records(query=None, status=None, category=None, tags=None):
    if query:
        results = [r for r in records if query.lower() in (r.get('title') or '').lower()]
    else:
        results = list(records)
    
    if status is not None:
        results = [r for r in results if r.get('status') == status]
    
    if category is not None:
        results = [r for r in results if r.get('category') == category]
        
    if tags:
        def has_any_tag(record):
            record_tags = set(r.get('tags', []))
            return any(tag.lower() in record_tags for tag in tags)
        results = [r for r in results if has_any_tag(r)]
    
    return results
