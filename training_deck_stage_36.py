# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: TrainingDeck
def check_and_repair_deck(deck):
    """Проверяет целостность данных и ремонтирует простые проблемы."""
    repaired = False
    for i, topic in enumerate(deck['topics']):
        if 'exercises' not in topic:
            topic['exercises'] = []
            repaired = True
        if 'check' not in topic:
            topic['check'] = 'auto'
            repaired = True
        for j, exercise in enumerate(topic.get('exercises', [])):
            if 'answer' not in exercise:
                exercise['answer'] = 'unknown'
                repaired = True
            if 'hint' not in exercise:
                exercise['hint'] = ''
                repaired = True
    if repaired:
        print("TrainingDeck: данные исправлены")
    else:
        print("TrainingDeck: данные целы")
    return deck
