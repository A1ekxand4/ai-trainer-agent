"""Тест полного цикла сохранения и загрузки."""

from pathlib import Path

from src.file_storage import init_storage, load_storage, save_storage


def test_full_storage_cycle(tmp_path: Path) -> None:
    """Тест: сохранение данных, затем их загрузка."""
    test_file = tmp_path / "cycle_test.json"
    init_storage(test_file)

    # Данные, которые мы хотим сохранить
    data = [{"type": "бег", "duration": 30}]

    # 1. Сохраняем
    save_storage(data)

    # 2. Загружаем и проверяем
    loaded_data = load_storage()
    assert loaded_data == data
