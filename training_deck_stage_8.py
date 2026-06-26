# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: TrainingDeck
def show_menu():
    print("\n=== TrainingDeck Menu ===")
    print("1. List Topics")
    print("2. View Exercises")
    print("3. Check Progress")
    print("4. Add New Topic/Exercise")
    print("5. Exit")
    choice = input("Select option (1-5): ").strip()
    if not choice.isdigit(): return None
    try:
        opt = int(choice)
        if opt == 1:
            for t in topics.values(): print(f"Topic: {t['title']} ({len(t.get('exercises', []))} exercises)")
        elif opt == 2:
            tid = input("Enter topic ID or name to view exercises: ").strip()
            target = next((t for t in topics.values() if t['id'] == tid or t['title'].lower() == tid.lower()), None)
            if not target: print("Topic not found.")
            else:
                print(f"\nExercises for '{target['title']}':")
                for ex in target.get('exercises', []):
                    status = "Done" if ex['completed'] else "Pending"
                    print(f"- {ex['instruction'][:30]}... [{status}]")
        elif opt == 3:
            total = sum(len(t.get('exercises', [])) for t in topics.values())
            done = sum(1 for t in topics.values() for ex in t.get('exercises', []) if ex['completed'])
            print(f"Progress: {done}/{total} exercises completed ({int(done/total*100)}%)")
        elif opt == 4:
            action = input("Add 'topic' or 'exercise': ").strip().lower()
            if action in ('topic', 'ex'):
                title = input("Enter new topic/exercise name: ").strip()
                print(f"Created placeholder for '{title}'. (Full implementation requires data structure update)")
            else:
                print("Invalid action.")
        elif opt == 5:
            print("Exiting...")
            return None
    except ValueError: pass
    input("\nPress Enter to continue...")
