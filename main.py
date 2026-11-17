"""Точка входа в приложение."""

from pathlib import Path

from src.cli import cli
from src.file_storage import init_storage, load_storage, save_storage
from src.tasks import get_trainings, init_trainings


def main() -> None:
    """Запуск приложения с загрузкой и сохранением состояния."""
    # 1. Инициализация хранилища
    init_storage(Path("data", "trainings.json"))

    # 2. Загрузка данных (при первом запуске вернется [])
    saved_trainings = load_storage()

    # 3. Передача данных в модуль логики
    init_trainings(saved_trainings)

    # 4. Запуск интерфейса
    cli()

    # 5. Сохранение данных при выходе
    save_storage(get_trainings())


if __name__ == "__main__":
    main()
