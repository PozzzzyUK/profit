# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: TrainingDeck
class UserProfiles:
    def __init__(self):
        self.profiles = {}

    def add_profile(self, name, level=1):
        self.profiles[name] = {"name": name, "level": level}

    def get_profile(self, name):
        return self.profiles.get(name)

    def remove_profile(self, name):
        if name in self.profiles:
            del self.profiles[name]
            return True
        return False
