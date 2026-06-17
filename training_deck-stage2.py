# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: TrainingDeck
class ValidationError(Exception): pass

def validate_int(value, min_val=None, max_val=None):
    try:
        v = int(value)
        if min_val is not None and v < min_val: raise ValidationError(f"Минимум {min_val}")
        if max_val is not None and v > max_val: raise ValidationError(f"Максимум {max_val}")
        return v
    except ValueError: raise ValidationError("Не целое число")

def validate_float(value, min_val=None):
    try:
        v = float(value)
        if min_val is not None and v < min_val: raise ValidationError(f"Минимум {min_val}")
        return v
    except ValueError: raise ValidationError("Не число с плавающей точкой")

def validate_positive_int(value, name="значение"):
    try:
        v = int(value)
        if v <= 0: raise ValidationError(f"{name} должно быть > 0")
        return v
    except ValueError: raise ValidationError(f"{name} должно быть целым числом")

def validate_string(value, min_len=1, max_len=None):
    s = str(value).strip()
    if len(s) < min_len: raise ValidationError(f"Минимум {min_len} символов")
    if max_len is not None and len(s) > max_len: raise ValidationError(f"Максимум {max_len} символов")
    return s

def validate_email(value):
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, value): raise ValidationError("Некорректный email")
    return value

def validate_date(value, fmt="%Y-%m-%d"):
    try:
        from datetime import datetime
        datetime.strptime(str(value), fmt)
        return str(value)
    except ValueError: raise ValidationError(f"Дата не в формате {fmt}")
