"""Интерфейс командной строки для ИИ-агента."""

from rich import print as rprint
from rich.markup import escape

from .tasks import add_training, delete_training, get_stats, list_trainings

HELP_TEXT = """Доступные команды:
[bold cyan]add <тип> <минуты>[/bold cyan] - добавить тренировку (пример: add бег 45)
[bold cyan]list[/bold cyan] - показать все тренировки
[bold cyan]stats[/bold cyan] - показать общую статистику
[bold cyan]delete <индекс>[/bold cyan] - удалить тренировку по номеру
[bold cyan]help[/bold cyan] - показать эту справку
[bold cyan]exit[/bold cyan] - выйти из программы"""


def cli() -> None:
    """Главный цикл обработки команд."""
    rprint(
        "[bold green]Добро пожаловать в ИИ-агент "
        "'Помощник по тренировкам'![/bold green]"
    )
    rprint("Введите 'help' для списка команд.")

    while True:
        try:
            user_input = input("\n> ").strip()
            if not user_input:
                continue

            parts = user_input.split()
            command = parts[0].lower()
            args = parts[1:]

            if command == "help":
                rprint(HELP_TEXT)
            elif command == "add":
                if len(args) != 2:
                    rprint(
                        "[bold red]Ошибка:[/bold red] неверное количество "
                        "аргументов. Используйте: add <тип> <время>"
                    )
                    continue

                training_type = args[0]
                try:
                    duration = int(args[1])
                    if duration <= 0:
                        rprint(
                            "[bold red]Ошибка:[/bold red] длительность "
                            "должна быть больше нуля."
                        )
                        continue
                except ValueError:
                    rprint(
                        "[bold red]Ошибка:[/bold red] длительность "
                        "должна быть целым числом."
                    )
                    continue

                add_training(training_type, duration)
                safe_type = escape(training_type)
                rprint(
                    f"[green]Успех![/green] Добавлена тренировка: "
                    f"{safe_type} на {duration} минут."
                )

            elif command == "list":
                print(list_trainings())
            elif command == "delete":
                if len(args) != 1:
                    rprint("[bold red]Ошибка:[/bold red] укажите индекс тренировки.")
                    continue
                try:
                    idx = int(args[0])
                    if delete_training(idx):
                        rprint("[green]Успех![/green] Тренировка удалена.")
                    else:
                        rprint("[bold red]Ошибка:[/bold red] тренировка не найдена.")
                except ValueError:
                    rprint("[bold red]Ошибка:[/bold red] индекс должен быть числом.")
            elif command == "stats":
                rprint(get_stats())
            elif command in ["exit", "quit"]:
                rprint("[italic]Завершение работы. До свидания![/italic]")
                break
            else:
                rprint(
                    "[bold red]Неизвестная команда.[/bold red] "
                    "Введите 'help' для справки."
                )

        except KeyboardInterrupt:
            # Обработка нажатия Ctrl+C для штатного выхода
            rprint("\n[italic]Завершение работы. До свидания![/italic]")
            break

        except Exception as e:
            # Перехват любых других непредвиденных ошибок, чтобы программа не падала
            safe_error = escape(str(e))
            rprint(
                f"[bold red]Произошла непредвиденная ошибка:[/bold red] {safe_error}"
            )
