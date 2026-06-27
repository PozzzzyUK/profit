# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: TrainingDeck
import json, sys

def load_initial_data(json_string):
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект")
        return {
            "topics": data.get("topics", []),
            "exercises": data.get("exercises", {}),
            "checks": data.get("checks", {}),
            "progress": data.get("progress", {})
        }
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return None

if __name__ == "__main__":
    sample_json = '''
{
  "topics": [
    {"id": 1, "title": "Базовый синтаксис", "description": "Переменные и типы"},
    {"id": 2, "title": "Условные конструкции", "description": "if/else"}
  ],
  "exercises": {
    "1.1": {"topic_id": 1, "question": "Что выведет print(5)?", "answer": "5"},
    "2.1": {"topic_id": 2, "question": "Результат if x > 0 else 0 при x=-1?", "answer": "0"}
  },
  "checks": {
    "1.1": ["print(5)"],
    "2.1": ["if x < 0: print(0)", "else: print(x)"]
  },
  "progress": {}
}'''

    deck = load_initial_data(sample_json)
    if deck:
        print(f"Загружено {len(deck['topics'])} тем и {len(deck['exercises'])} упражнений.")
