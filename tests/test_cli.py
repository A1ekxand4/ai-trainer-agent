"""Тесты для интерфейса командной строки (src/cli.py)."""

import pytest

from src import cli
from src.tasks import get_trainings, init_trainings


@pytest.fixture(autouse=True)
def clear_state() -> None:
    """Очистка состояния перед каждым тестом."""
    init_trainings([])


def test_cli_add_and_exit(monkeypatch) -> None:
    """Тест добавления тренировки и выхода."""
    inputs = iter(["add бег 30", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    cli.cli()

    assert len(get_trainings()) == 1
    assert get_trainings()[0]["type"] == "бег"


def test_cli_invalid_inputs(monkeypatch) -> None:
    """Тест обработки ошибочного ввода."""
    inputs = iter(["unknown", "add", "add бег много", "add бег -5", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    cli.cli()

    assert len(get_trainings()) == 0


def test_cli_list_and_stats(monkeypatch) -> None:
    """Тест команд list и stats."""
    init_trainings([{"type": "бег", "duration": 30}])
    inputs = iter(["list", "stats", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    cli.cli()
