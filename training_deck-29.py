# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: TrainingDeck
def load_config():
    """Загружает конфигурацию из словаря по умолчанию."""
    return {
        "app_name": "TrainingDeck",
        "version": 1,
        "max_attempts_per_exercise": 3,
        "progress_tracking": True,
        "difficulty_levels": ["easy", "medium", "hard"],
        "default_difficulty": "easy",
    }

def get_config():
    """Получает текущую конфигурацию приложения."""
    if not hasattr(load_config.__module__, "_config_cache"):
        load_config.__module__._config_cache = load_config()
    return load_config.__module__._config_cache
