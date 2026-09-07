# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: TrainingDeck
def color(text, code):
    return "\033[" + str(code) + "m" + text + "\033[0m"

COLORS = {
    "red": "31", "green": "32", "yellow": "33", "blue": "34",
    "magenta": "35", "cyan": "36", "white": "37",
    "bold": "1", "dim": "2", "underline": "4",
}

def styled(text, **kwargs):
    parts = []
    for key, val in COLORS.items():
        if key in kwargs:
            parts.append(val)
            kwargs.pop(key)
    if not parts:
        return text
    return "\033[" + "".join(parts) + "m" + text + "\033[0m"

class Ansi:
    def red(self, text):   return styled(text, red=True)
    def green(self, text):  return styled(text, green=True)
    def yellow(self, text): return styled(text, yellow=True)
    def blue(self, text):   return styled(text, blue=True)
    def magenta(self, text):return styled(text, magenta=True)
    def cyan(self, text):   return styled(text, cyan=True)
    def bold(self, text):   return styled(text, bold=True)
    def dim(self, text):    return styled(text, dim=True)
    def underline(self, text):return styled(text, underline=True)
    def reset(self):        return "\033[0m"
    def __getattr__(self, name):
        raise AttributeError(f"No such attribute: {name}")

ANSI = Ansi()

def disable_ansi():
    import os
    os.environ["NO_COLOR"] = "1"

def enable_ansi():
    import os
    os.environ.pop("NO_COLOR", None)
