# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: TrainingDeck
import argparse

def main():
    parser = argparse.ArgumentParser(description="TrainingDeck CLI")
    sub = parser.add_subparsers(dest="command")

    p = sub.add_parser("start", help="Запустить приложение")
    p.set_defaults(func=lambda _: start_app())

    p = sub.add_parser("reset", help="Сбросить прогресс")
    p.add_argument("--path", default="progress.json")
    p.set_defaults(func=lambda a: reset_progress(a.path))

    p = sub.add_parser("status", help="Показать прогресс")
    p.set_defaults(func=lambda _: show_status())

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
