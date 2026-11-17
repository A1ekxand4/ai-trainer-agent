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
