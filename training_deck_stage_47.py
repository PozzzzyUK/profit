# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: TrainingDeck
def demo():
    print("=" * 50)
    print("TrainingDeck Demo")
    print("=" * 50)

    deck = TrainingDeck()

    deck.add_theme("Python Basics")
    deck.add_theme("Data Structures")

    deck.add_exercise("Python Basics", "Variables & Types", "print('Hello')",
                      lambda: True, "Correct!", "Try again")
    deck.add_exercise("Python Basics", "Strings", "s = 'Hello World'\nprint(len(s))",
                      lambda: True, "Correct!", "Try again")
    deck.add_exercise("Data Structures", "Lists", "nums = [1, 2, 3]\nprint(sum(nums))",
                      lambda: True, "Correct!", "Try again")

    print("\n📚 Available themes:")
    for t in deck.themes:
        print(f"  • {t}")

    print("\n🏋️ Exercises:")
    for exc in deck.exercises:
        print(f"  • {exc.name} ({exc.difficulty})")

    print("\n🧪 Running checks...")
    for exc in deck.exercises:
        result = exc.check()
        print(f"  • {exc.name}: {result}")

    print("\n✅ Demo complete!")
