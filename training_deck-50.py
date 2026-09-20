# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: TrainingDeck
def polish_messages():
    """Настройка финальных текстов для всех уведомлений."""
    messages = {
        "start": "Добро пожаловать в TrainingDeck! Вы готовы к обучению.",
        "theme_selected": "Тема выбрана: {theme}",
        "exercise_started": "Начинаем упражнение: {exercise}",
        "exercise_completed": "Отлично! Вы успешно решили упражнение: {exercise}",
        "exercise_failed": "Не удалось. Попробуйте ещё раз упражнение: {exercise}",
        "progress_updated": "Прогресс обновлён: вы прошли {count} из {total} упражнений",
        "session_ended": "Сессия завершена. Всего пройдено: {count} из {total} упражнений",
        "invalid_input": "Пожалуйста, введите корректный ответ.",
        "quit": "До свидания! Хороших результатов в обучении!",
    }
    return messages
