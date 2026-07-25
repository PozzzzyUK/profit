# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: TrainingDeck
def reset_demo_data():
    """Сбрасывает все демо-данные в начальные значения."""
    global deck, current_topic, exercises_done, exercise_log
    
    deck = {
        'intro': {'name': 'Введение', 'exercises': [
            {'id': 'e1', 'task': 'Приветствие', 'check': lambda x: str(x).strip() == 'Hello'},
            {'id': 'e2', 'task': 'Команда', 'check': lambda x: str(x).strip().lower() in ['python', 'code']},
        ]}
    }
    
    current_topic = None
    exercises_done = set()
    exercise_log = []

def clear_progress():
    """Очищает прогресс и текущее состояние."""
    global deck, current_topic, exercises_done, exercise_log
    
    deck = {}
    current_topic = None
    exercises_done = set()
    exercise_log = []

if __name__ == '__main__':
    print("Демо-данные сброшены")
    reset_demo_data()
    print(f"Текущая тема: {current_topic}")  # None
    print(f"Прогресс: {exercises_done}")       # set()
    print("Готов к запуску нового плана!")
