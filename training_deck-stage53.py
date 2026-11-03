# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: TrainingDeck
import re

def parse_records(text):
    lines = [ln for ln in text.splitlines() if ln.strip()]
    records = []
    for ln in lines:
        m = re.match(r"(\w+)\s*-\s*(\w+)\s*::\s*(\w+)\s*::\s*(\d+)", ln)
        if m:
            records.append({
                "topic": m.group(1),
                "exercise": m.group(2),
                "check": m.group(3),
                "attempts": int(m.group(4)),
            })
    return records

def export_records(path, records):
    with open(path, "w", encoding="utf-8") as f:
        for r in records:
            f.write(f"{r['topic']} - {r['exercise']} :: {r['check']} :: {r['attempts']}\n")

def import_records(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        return []
    return parse_records(text)
