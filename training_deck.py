# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: TrainingDeck
import json
from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import Optional

@dataclass
class Exercise:
    id: int
    title: str
    description: str
    difficulty: str = "easy"
    
@dataclass 
class Check:
    question: str
    expected_answer: str
    
@dataclass
class Topic:
    name: str
    exercises: list[Exercise] = field(default_factory=list)
    checks: list[Check] = field(default_factory=list)

@dataclass
class UserProgress:
    completed_exercises: set[int] = field(default_factory=set)
    last_login: Optional[str] = None
    
def init_training_deck():
    deck_data = {
        "topics": [
            Topic(
                name="Основы Python",
                exercises=[
                    Exercise(id=1, title="Приветствие", description="Напечатай 'Hello World'"),
                    Exercise(id=2, title="Переменные", description="Создай переменную age и присвой ей 25")
                ],
                checks=[Check(question="Что выведет print('Hello')?", expected_answer="Hello")]
            ),
            Topic(
                name="Структуры данных",
                exercises=[
                    Exercise(id=3, title="Списки", description="Создай список из трёх чисел"),
                    Exercise(id=4, title="Словари", description="Создай словарь с ключом 'name' и значением 'Alice'")
                ],
                checks=[]
            )
        ]
    }
    
    with open("training_deck.json", "w", encoding="utf-8") as f:
        json.dump(deck_data, f, ensure_ascii=False, indent=2)
        
    return deck_data

if __name__ == "__main__":
    init_training_deck()
