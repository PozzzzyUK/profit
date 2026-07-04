# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: TrainingDeck
def search_materials(query, fields=None):
    if not query:
        return list(materials.values())
    
    query = query.lower().strip()
    if fields is None:
        fields = ['title', 'topic', 'description']
    
    results = []
    for item_id, material in materials.items():
        match_found = False
        search_fields = fields or list(material.keys())
        
        for field_name in search_fields:
            value = str(getattr(material, field_name, ''))
            if query in value.lower():
                match_found = True
                break
        
        if match_found:
            results.append(item_id)
    
    return results
