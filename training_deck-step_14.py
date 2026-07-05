# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: TrainingDeck
def generate_summary(deck):
    total_topics = len(deck['topics'])
    completed_exercises = sum(1 for t in deck['topics'] for e in t['exercises'] if e.get('completed', False))
    pending_exercises = sum(1 for t in deck['topics'] for e in t['exercises'] if not e.get('completed', False))
    
    print(f"=== Сводка TrainingDeck ===")
    print(f"Всего тем: {total_topics}")
    print(f"Выполнено упражнений: {completed_exercises}")
    print(f"Осталось упражнений: {pending_exercises}")
    
    if deck.get('user_progress', {}):
        total_time = sum(p.get('time_spent_seconds', 0) for p in deck['user_progress'].values())
        hours = total_time / 3600
        print(f"Всего затрачено времени: {hours:.1f} часов")
    
    print("===========================")
