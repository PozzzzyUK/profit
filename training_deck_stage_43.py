# === Stage 43: Добавь пагинацию длинных списков ===
# Project: TrainingDeck
def paginate(data, page_size=10):
    """Делит список на страницы."""
    if not data:
        return []
    pages = []
    for i in range(0, len(data), page_size):
        pages.append(data[i:i + page_size])
    return pages
