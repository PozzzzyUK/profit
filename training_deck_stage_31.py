# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: TrainingDeck
def switch_profile():
    if not user_profiles or len(user_profiles) == 0:
        print("Нет доступных профилей.")
        return
    current = next((p for p in user_profiles if p['is_active']), None)
    print(f"Текущий профиль: {current['name']}" if current else "Нет активного профиля.")
    while True:
        name = input("Введите имя нового профиля или 'done' для возврата: ").strip()
        if name == 'done':
            break
        target = next((p for p in user_profiles if p['name'].lower() == name.lower()), None)
        if not target:
            print(f"Профиль '{name}' не найден.")
            continue
        for p in user_profiles:
            p['is_active'] = False
        target['is_active'] = True
        current_name = current['name'] if current else 'Никто'
        print(f"Переключено с {current_name} на {target['name']}.")
