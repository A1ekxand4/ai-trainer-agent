"""Модуль для работы с данными тренировок."""

# Глобальное состояние, которое мы будем инициализировать извне
_trainings: list[dict] = []


def init_trainings(trainings: list[dict]) -> None:
    """Инициализация списка тренировок."""
    global _trainings
    _trainings = trainings


def get_trainings() -> list[dict]:
    """Получение списка тренировок."""
    return _trainings


def add_training(training_type: str, duration: int) -> None:
    """Добавляет тренировку в список."""
    _trainings.append({"type": training_type, "duration": duration})


def list_trainings() -> str:
    """Возвращает форматированный список тренировок."""
    if not _trainings:
        return "Список тренировок пуст. Добавьте первую тренировку!"

    output = "--- Ваши тренировки ---\n"
    for index, training in enumerate(_trainings):
        output += f"{index}. {training['type']} - {training['duration']} мин.\n"
    return output


def get_stats() -> str:
    """Возвращает общую статистику."""
    if not _trainings:
        return "Статистика пуста. Нет данных о тренировках."

    total_time = sum(t["duration"] for t in _trainings)
    return f"\nВсего тренировок: {len(_trainings)}\nОбщее время: {total_time} минут\n"


def delete_training(index: int) -> bool:
    """Удаляет тренировку по индексу. Возвращает True при успехе."""
    if 0 <= index < len(_trainings):
        _trainings.pop(index)
        return True
    return False
