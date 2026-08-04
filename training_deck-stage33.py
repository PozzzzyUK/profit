# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: TrainingDeck
python
import copy

def undo_last_action(deck):
    """Откатывает последнее действие: если пользователь ошибся в проверке,
    возвращает упражнение с пустым ответом, но сохраняет его как решённое."""
    if not deck.get("history"):
        return deck
    last = deck["history"][-1]
    exercise_id = last.get("exercise_id")
    if not exercise_id:
        return deck
    exercises = deck.setdefault("exercises", {})
    ex = copy.deepcopy(exercises.get(exercise_id, {}))
    # Восстанавливаем исходный вопрос
    original = ex.pop("_original_q", None)
    if original is None and "q" in ex:
        original = ex.pop("q")
    exercises[exercise_id] = {"q": original, "_solved": True}
    deck["history"].pop()
    return deck
