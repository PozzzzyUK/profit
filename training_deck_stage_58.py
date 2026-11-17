# === Stage 58: Добавь простую систему пользовательских представлений списка ===
# Project: TrainingDeck
class ViewManager:
    def __init__(self):
        self._views = []
        self._current = None

    def register(self, name, func):
        self._views[name] = func

    def view(self, name):
        if name not in self._views:
            raise KeyError(f"Unknown view: {name}")
        self._current = name
        return self._views[name]

    def switch(self, name):
        if name in self._views:
            self._current = name
            return True
        return False

    def current(self):
        return self._current

    def is_empty(self):
        return len(self._views) == 0

    def names(self):
        return list(self._views.keys())
