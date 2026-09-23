# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: TrainingDeck
def export_report(deck, filepath="report.txt"):
    lines = []
    lines.append("=== TrainingDeck Report ===")
    lines.append(f"Topics: {len(deck.topics)}")
    lines.append(f"Exercises: {len(deck.exercises)}")
    lines.append(f"Checks: {len(deck.checks)}")
    lines.append(f"Progress: {len(deck.progress)}")
    lines.append("")
    lines.append("--- Topics ---")
    for t in deck.topics:
        lines.append(f"- {t.name}: {t.description}")
    lines.append("")
    lines.append("--- Exercises ---")
    for e in deck.exercises:
        lines.append(f"- {e.name} ({e.difficulty}): {e.description}")
    lines.append("")
    lines.append("--- Checks ---")
    for c in deck.checks:
        lines.append(f"- {c.name}: {c.description}")
    lines.append("")
    lines.append("--- Progress ---")
    for p in deck.progress:
        lines.append(f"- {p.name}: {p.status}")
    with open(filepath, "w") as f:
        f.write("\n".join(lines))
