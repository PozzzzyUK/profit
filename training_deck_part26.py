# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: TrainingDeck
def run_demo():
    """Демо-команды для ручного тестирования TrainingDeck."""
    import sys, os
    
    script_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in dir() else os.getcwd()
    
    # Имитация запуска с демо-аргументами
    args = [
        "TrainingDeck",
        "--demo",
        "--theme", "python_basics",
        "--exercise", "print_hello",
        "--check", "assert_print_hello",
        "--progress"
    ]
    
    # Запуск с демо-аргументами
    sys.argv = args
    
    from training_deck import TrainingDeck, Theme, Exercise, Check, ProgressTracker
    
    deck = TrainingDeck(script_dir)
    
    # Демо тема
    demo_theme = Theme(
        name="python_basics",
        description="Основы Python",
        exercises=[
            Exercise("print_hello", "Выведите 'Hello World'", "assert_print_hello"),
            Exercise("type_check", "Проверьте тип int", "assert_type_check")
        ]
    )
    
    deck.add_theme(demo_theme)
    
    # Демо упражнение
    exercise = Exercise(
        name="print_hello_demo",
        code='print("Hello World")',
        check='import sys; assert "Hello World" in sys.stdout.getvalue()',
        hint="Напечатайте Hello World"
    )
    
    deck.add_exercise(exercise)
    
    # Демо прогресс
    progress = ProgressTracker()
    progress.record(1, 2, 'python_basics', 'print_hello')
    progress.record(0, 0, 'python_basics', 'type_check')
    
    print("=== TrainingDeck Demo ===")
    print(f"Добавлено тем: {deck.theme_count}")
    print(f"Добавлено упражнений: {deck.exercise_count}")
    print(f"Прогресс: {progress.get_stats()}")
    
    return deck, progress


if __name__ == "__main__":
    run_demo()
