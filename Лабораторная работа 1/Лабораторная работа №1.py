# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class Car:
    def __init__(self, engine_power: float, weight: float):
        """
        Создание и подготовка к работе объекта транспортное средство

        :param engine_power: мощность двигателя в л.с
        :param weight: вес транспортного средства в снаряженном состоянии, кг

        :raise TypeError: возникает при отличном от int и float типе engine_power или weight
        :raise ValueError: возникает в случае нулевого или отрицательного значения у engine_power или weight

        Примеры:
        >>> car1 = Car(150, 1500) # иницализация экземпляра класса
        """
        if not isinstance(engine_power, (int, float)):
            raise TypeError('Мощность двигателя это число')
        if not isinstance(weight, (int, float)):
            raise TypeError('Вес транспортного средства это число')
        if engine_power <= 0:
            raise ValueError('Мощность двигателя это положительное число')
        if weight <= 0:
            raise ValueError('Вес транспортного средства это положительное число')
        self.engine_power = engine_power
        self.weight = weight

    def specific_power_of_car(self) -> float:
        """
        Удельная мощность транспортного средства

        :return: коэффициент удельной мощности т.с.

        Примеры:
        >>> car = Car(150,1500)
        >>> car.specific_power_of_car()

        """

        ...

    def tax_characters_of_car(self, passing_capacity: float) -> str:
        """
        Налоговые характеристики транспортного средства

        :param passing_capacity: доналоговая мощность т.с.

        :return: Является ли т.с. проходным по мощности и категория т.с.

        :raise TypeError: возникает при отличном от int и float типе passing_capacity
        :raise ValueError: При вводе некорректной доналоговой мощности т.с. возвращается ошибка

        Примеры:
        >>> car = Car(300,3700)
        >>> car.tax_characters_of_car(160)
        """
        if not isinstance(passing_capacity, (int, float)):
            raise TypeError('доналоговая мощность это число')
        if passing_capacity <= 0:
            raise ValueError('доналоговая мощность это положительное число')

        ...


class Computer:
    def __init__(self, RAM_memory: int, ROM_memory: int):
        """
        Создание и подготовка к работе объекта компьютер

        :param RAM_memory: оперативная память, ГБ
        :param ROM_memory:  внутренняя память, ГБ

        :raise TypeError: возникает при отличном от int и float типе RAM_memory или ROM_memory
        :raise ValueError: возникает в случае нулевого или отрицательного значения у RAM_memory или ROM_memory

        Примеры:
        >>> msi = Computer(64, 1024) # инициализация экземпляра класса
        """
        if not isinstance(RAM_memory, (int, float)):
            raise TypeError("Оперативная память должна быть типа int или float")
        if RAM_memory <= 0:
            raise ValueError("Оперативная память должна быть положительным числом")
        self.RAM_memory = RAM_memory

        if not isinstance(ROM_memory, (int, float)):
            raise TypeError("Внутренняя память должна быть типа int или float")
        if ROM_memory <= 0:
            raise ValueError("Внутренняя память должна быть положительным числом")
        self.ROM_memory = ROM_memory

    def increased_memory(self, added_RAM_memory: int, added_ROM_memory: int) -> int:
        """
        Увеличение памяти

        :param added_RAM_memory: добавленная оперативная память
        :param added_ROM_memory:  добавленная внутренняя память

        :return: показатели обновленной конфигурации ПК

        :raise TypeError: при вводе показателей добавленной памяти отличных от int или float возвращается ошибка
        :raise ValueError: возникает в случае нулевого или отрицательного значения у added_RAM_memory или added_ROM_memory

        Примеры:
        >>> HP = Computer(32, 1024)
        >>> HP.increased_memory(16, 512)
        """
        if not isinstance(added_RAM_memory, (int, float)):
            raise TypeError("Добавленная оперативная память должна быть типа int или float")
        if added_RAM_memory <= 0:
            raise ValueError("Добавленная оперативная память должна быть положительным числом")

        if not isinstance(added_ROM_memory, (int, float)):
            raise TypeError("Добавленная внутренняя память должна быть типа int или float")
        if added_ROM_memory <= 0:
            raise ValueError("Добавленная внутренняя память должна быть положительным числом")


        ...

    def minimum_requirements(self, programm: str, dict_requirements: dict) -> str:
        """
        Минимальные требования к объему RAM

        :param programm: программа из заданного словаря, с минимальными требованиями по RAM
        :param dict_requirements: словарь программ с минимальными требованиями по RAM

        :return: строка о соответвствии/несоответствии минимальным требованиям

        :raise TypeError: выводится в случае отсутствия программы в словаре или вводе программы и словаря
        отличными от типа str и dict соответственно

        Примеры:
        >>> mac = Computer(16, 1024)
        >>> mac.minimum_requirements('PyCharm', {'PyCharm' : 8, 'Yandex' : 16, 'Revit' : 32})
        """
        if not isinstance(programm, str) and not isinstance(dict_requirements, dict):
            raise TypeError('Несоответствие программы или словаря типам str и dict соответственно')
        if not programm in dict_requirements:
            raise TypeError('Программа не найдена в словаре')

        ...


class Barbell:
    def __init__(self, barbell_weight: int):
        """
        Создание и инициализация объекта штанга

        :param barbell_weight: текущий вес штанги с блинами

        :raise TypeError: возникает при несоответствии характеристики barbell_weight типу int или float
        :raise ValueError: возникает при не положительном переданном параметре barbell weight

        Примеры:
        >>> barbell = Barbell(20) # инициализация экземпляра класса
        """
        if not isinstance(barbell_weight, (int, float)):
            raise TypeError("Вес штанги должен быть типа int или float")
        if barbell_weight <= 0:
            raise ValueError("Вес штанги должен быть положительным числом")
        self.barbell_weight = barbell_weight

    def weight_before_target(self, target: int) -> int:
        """
        Вес требуемый до заданной цели

        :param target: цель по весу на штанге

        :return: вес необходимый, чтобы достичь цели

        :raise TypeError: возникает при несоответствии характеристики target типу int или float
        :raise ValueError: возникает при не положительном переданном параметре target

        Примеры:
        >>> barbell = Barbell(100)
        >>> barbell.weight_before_target(200)
        """
        if not isinstance(target, (int, float)):
            raise TypeError("Цель должна быть типа int или float")
        if target <= 0:
            raise ValueError("Цель должна быть положительным числом")

        ...

    def target_weight(self, added_weight: int) -> int:
        """
        Конечный вес на штанге

        :param added_weight:  добавленный вес

        :return: Конечный вес на штанге

        :raise TypeError: возникает при несоответствии характеристики added_weight типу int или float
        :raise ValueError: возникает при не положительном переданном параметре added_weight

        Примеры:
        >>> barbell = Barbell(20)
        >>> barbell.target_weight(120)

        """
        if not isinstance(added_weight, (int, float)):
            raise TypeError("Добавленный вес должен быть типа int или float")
        if added_weight <= 0:
            raise ValueError("Добавленный вес должен быть положительным числом")

        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации