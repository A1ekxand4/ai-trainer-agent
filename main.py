"""Точка входа в приложение."""

from pathlib import Path

from src.cli import cli
from src.file_storage import init_storage, load_storage, save_storage
from src.tasks import get_trainings, init_trainings


def main() -> None:
    """Запуск приложения с загрузкой и сохранением состояния."""
    init_storage(Path("data", "trainings.json"))

    saved_trainings = load_storage()

    # Если при загрузке произошла ошибка (вернулся None),
    # мы не должны перезаписывать поврежденный файл.
    if saved_trainings is None:
        saved_trainings = []  # для работы в памяти
        disable_saving = True
    else:
        disable_saving = False

    init_trainings(saved_trainings)
    cli()

    if not disable_saving:
        save_storage(get_trainings())


if __name__ == "__main__":
    main()
