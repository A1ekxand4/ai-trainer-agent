"""Модуль для работы с данными тренировок."""

# Глобальное состояние (хранение в памяти)
TRAININGS: list[dict] = []


def add_training(training_type: str, duration: int) -> None:
    """Добавляет тренировку в список."""
    TRAININGS.append({"type": training_type, "duration": duration})


def list_trainings() -> str:
    """Возвращает форматированный список тренировок."""
    if not TRAININGS:
        return "Список тренировок пуст. Добавьте первую тренировку!"
    
    output = "--- Ваши тренировки ---\n"
    for index, training in enumerate(TRAININGS):
        output += f"{index}. {training['type']} - {training['duration']} мин.\n"
    return output


def get_stats() -> str:
    """Возвращает общую статистику."""
    if not TRAININGS:
        return "Статистика пуста. Нет данных о тренировках."
    
    total_time = sum(t["duration"] for t in TRAININGS)
    return (
        f"\nВсего тренировок: {len(TRAININGS)}\n"
        f"Общее время: {total_time} минут\n"
    )
