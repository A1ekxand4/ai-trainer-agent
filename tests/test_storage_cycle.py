"""Тесты полного цикла сохранения, загрузки и удаления."""

from pathlib import Path

from src.file_storage import init_storage, load_storage, save_storage
from src.tasks import add_training, delete_training, get_trainings, init_trainings


def test_full_cycle_with_delete(tmp_path: Path) -> None:
    """Сценарий: сохранение, загрузка и удаление записи."""
    test_file = tmp_path / "cycle_test.json"
    init_storage(test_file)
    init_trainings([])

    # Добавляем тренировки
    add_training("бег", 30)
    add_training("плавание", 45)

    # Сохраняем (как main.py при выходе)
    save_storage(get_trainings())
    assert test_file.exists()

    # Загружаем (как main.py при старте)
    loaded = load_storage()
    init_trainings(loaded)
    assert len(get_trainings()) == 2

    # Удаляем первую и сохраняем снова
    assert delete_training(0) is True
    save_storage(get_trainings())

    # Проверяем, что в файле осталась только одна запись
    loaded_after_delete = load_storage()
    assert len(loaded_after_delete) == 1
    assert loaded_after_delete[0]["type"] == "плавание"


def test_load_broken_json(tmp_path: Path) -> None:
    """Тест: программа не падает при поврежденном JSON."""
    test_file = tmp_path / "broken.json"
    init_storage(test_file)

    # Пишем мусор
    with test_file.open("w", encoding="utf-8") as f:
        f.write("{broken: ")

    # load_storage должен вернуть None или пустой список, но не упасть
    result = load_storage()
    assert result is None or result == []
