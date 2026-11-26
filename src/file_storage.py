"""Модуль для сохранения и загрузки данных в формате JSON."""

import json
from pathlib import Path

# Приватная переменная для хранения пути к файлу по умолчанию
_storage_path = Path("data", "trainings.json")


def init_storage(path: Path) -> None:
    """Инициализация хранилища (установка пути)."""
    global _storage_path
    _storage_path = path
    # Создаем папку, если её нет
    _storage_path.parent.mkdir(parents=True, exist_ok=True)


def save_storage(data: list[dict]) -> None:
    """Сохранение данных в файл."""
    with _storage_path.open("w", encoding="utf-8") as file:
        # ensure_ascii=False чтобы кириллица в файле читалась нормально
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_storage() -> list[dict] | None:
    """Загрузка данных из файла. Возвращает None при ошибке."""
    try:
        with _storage_path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        # Если файла нет (первый запуск) — возвращаем пустой список
        return []
    except json.JSONDecodeError:
        # Если файл поврежден, выводим сообщение и возвращаем None
        print(
            f"Ошибка: файл {_storage_path} поврежден. "
            "Загружен пустой список, сохранение отключено."
        )
        return None
