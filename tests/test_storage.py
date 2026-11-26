"""Тесты для модуля хранения (src/file_storage.py)."""

from pathlib import Path

from src.file_storage import init_storage, load_storage, save_storage


def test_save_and_load(tmp_path: Path) -> None:
    """Тест сохранения и загрузки данных."""
    test_file = tmp_path / "test_data.json"
    init_storage(test_file)

    # 1. Проверка первого запуска (файла нет)
    assert load_storage() == []

    # 2. Сохранение
    data = [{"type": "бег", "duration": 30}]
    save_storage(data)

    # 3. Проверка, что файл создался
    assert test_file.exists()

    # 4. Загрузка и проверка
    loaded = load_storage()
    assert loaded == data


def test_load_broken_json(tmp_path: Path) -> None:
    """Тест загрузки поврежденного JSON-файла."""
    test_file = tmp_path / "broken.json"
    init_storage(test_file)

    with test_file.open("w", encoding="utf-8") as f:
        f.write("{broken: ")

    # Теперь функция должна вернуть None (чтобы main.py не сохранял пустоту)
    assert load_storage() is None
