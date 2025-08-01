from typing import Dict, Type


class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(
        self,
        training_type: str,
        duration: float,
        distance: float,
        speed: float,
        calories: float,
    ) -> None:

        self.training_type: str = training_type
        self.duration: float = duration
        self.distance: float = distance
        self.speed: float = speed
        self.calories: float = calories

    def get_message(self) -> str:
        """Вывод сообщения в консоль"""
        return (
            f"Тип тренировки: {self.training_type}; "
            f"Длительность: {self.duration:.3f} ч.; "
            f"Дистанция: {self.distance:.3f} км; "
            f"Ср. скорость: {self.speed:.3f} км/ч; "
            f"Потрачено ккал: {self.calories:.3f}."
        )


class Training:
    """Базовый класс тренировки."""

    LEN_STEP: float = 0.65
    M_IN_KM: float = 1000
    MIN_IN_HOUR: int = 60

    def __init__(self, action: int, duration: float, weight: float) -> None:
        self.action: int = action
        self.duration: float = duration
        self.weight: float = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance: float = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_spead: float = self.get_distance() / self.duration
        return mean_spead

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(
            self.__class__.__name__,
            self.duration,
            self.get_distance(),
            self.get_mean_speed(),
            self.get_spent_calories(),
        )


class Running(Training):
    """Тренировка: бег."""

    CALORIES_MEAN_SPEED_MULTIPLIER: int = 18
    CALORIES_MEAN_SPEED_SHIFT: float = 1.79

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий при беге."""
        spent_calories = ((self.CALORIES_MEAN_SPEED_MULTIPLIER
                           * self.get_mean_speed()
                           + self.CALORIES_MEAN_SPEED_SHIFT)
                          * self.weight / self.M_IN_KM
                          * (self.duration * self.MIN_IN_HOUR))
        return spent_calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    CALORIES_WEIGHT_MULTIPLIER: float = 0.035
    CALORIES_SPEED_HEIGHT_MULTIPLIER: float = 0.029
    CM_IN_M: int = 100
    KMH_IN_MSEC: float = 0.278

    def __init__(
        self, action: int, duration: float, weight: float, height: int
    ) -> None:
        super().__init__(action, duration, weight)
        self.height: int = height

    """Получить количество затраченных калорий при спортивной ходьбе."""
    def get_spent_calories(self) -> float:
        spent_calories = ((self.CALORIES_WEIGHT_MULTIPLIER * self.weight
                           + ((self.get_mean_speed() * self.KMH_IN_MSEC) ** 2
                              / (self.height / self.CM_IN_M))
                          * self.CALORIES_SPEED_HEIGHT_MULTIPLIER
                          * self.weight) * (self.duration * self.MIN_IN_HOUR))
        return spent_calories


class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP: float = 1.38
    CALORIES_MEAN_SPEED_SHIFT: float = 1.1
    CALORIES_WEIGHT_MULTIPLIER: int = 2

    def __init__(
        self,
        action: int,
        duration: float,
        weight: float,
        length_pool: float,
        count_pool: int,
    ) -> None:
        super().__init__(action, duration, weight)
        self.lenght_pool: float = length_pool
        self.count_pool: int = count_pool

    def get_mean_speed(self):
        mean_speed: float = (
            self.lenght_pool * self.count_pool / self.M_IN_KM / self.duration
        )
        return mean_speed

    def get_spent_calories(self):
        spent_calories: float = (
            (self.get_mean_speed() + self.CALORIES_MEAN_SPEED_SHIFT)
            * self.CALORIES_WEIGHT_MULTIPLIER
            * self.weight
            * self.duration
        )
        return spent_calories


def read_package(workout_type: str, data: list) -> Training:
    # Функция возвращает объект класса Training (или его наследника).
    """Прочитать данные полученные от датчиков."""
    workout_dict: Dict[str, Type[Training]] = {
        "SWM": Swimming,
        "RUN": Running,
        "WLK": SportsWalking,
    }

    if workout_type not in workout_dict:
        return f"Неизвестный тип тренировки {workout_type}"
    return workout_dict[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == "__main__":
    packages = [
        ("SWM", [720, 1, 80, 25, 40]),
        ("RUN", [15000, 1, 75]),
        ("WLK", [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
