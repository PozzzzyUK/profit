# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: TrainingDeck
def print_table(headers, rows):
    col_widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            if len(str(val)) > col_widths[i]:
                col_widths[i] = len(str(val))

    fmt = " | ".join(f"{{:<{w}}}" for w in col_widths)
    header_line = fmt.format(*headers)
    sep_line = "-+-".join("-" * w for w in col_widths)
    print(header_line)
    print(sep_line)
    for row in rows:
        print(fmt.format(*row))

print_table(["Тема", "Упр.", "Результат"], [
    ("ОС", 1, "Прошло"),
    ("Матрица", 3, "Не пройдено"),
])
