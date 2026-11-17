"""Тесты для модуля логики (src/tasks.py)."""

import pytest

from src.tasks import add_training, get_trainings, init_trainings, list_trainings


@pytest.fixture(autouse=True)
def clear_state() -> None:
    """Очистка состояния перед каждым тестом."""
    init_trainings([])


def test_add_training() -> None:
    add_training("бег", 30)
    assert len(get_trainings()) == 1
    assert get_trainings()[0]["type"] == "бег"
    assert get_trainings()[0]["duration"] == 30


def test_list_empty() -> None:
    assert list_trainings() == "Список тренировок пуст. Добавьте первую тренировку!"


def test_list_not_empty() -> None:
    add_training("бег", 30)
    assert "0. бег - 30 мин." in list_trainings()
