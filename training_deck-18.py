# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: TrainingDeck
def add_tag(item_id, tag):
    for item in _items:
        if item.id == item_id and tag not in item.tags:
            item.tags.append(tag)
            return True
    raise ValueError(f"Item {item_id} not found")


def remove_tag(item_id, tag):
    for item in _items:
        if item.id == item_id and tag in item.tags:
            item.tags.remove(tag)
            return True
    raise ValueError(f"Tag '{tag}' not found on item {item_id}")
