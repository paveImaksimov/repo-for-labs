if __name__ == "__main__":
    import math


    class Shape:
        """
        Базовый класс для всех геометрических фигур.

        Атрибуты:
            _color (str): цвет фигуры
            _name (str): название фигуры
            _position_x (float): координата X центра фигуры
            _position_y (float): координата Y центра фигуры
        """

        def __init__(self, color: str, name: str, position_x: float = 0, position_y: float = 0) -> None:
            """
            Инициализация базовой фигуры.

            Args:
                color: цвет фигуры
                name: название фигуры
                position_x: координата X центра
                position_y: координата Y центра
            """
            self._color = color
            self._name = name
            self._position_x = position_x
            self._position_y = position_y

        def get_color(self) -> str:
            """
            Получение цвета фигуры.

            Returns:
                str: текущий цвет фигуры
            """
            return self._color

        def set_color(self, color: str) -> None:
            """
            Установка цвета фигуры.

            Args:
                color: новый цвет фигуры
            """
            self._color = color

        def move(self, delta_x: float, delta_y: float) -> None:
            """
            Перемещение фигуры.

            Args:
                delta_x: смещение по оси X
                delta_y: смещение по оси Y
            """
            self._position_x += delta_x
            self._position_y += delta_y

        def get_position(self) -> tuple[float, float]:
            """
            Получение текущей позиции фигуры.

            Returns:
                tuple[float, float]: координаты (x, y) центра фигуры
            """
            return (self._position_x, self._position_y)

        def area(self) -> float:
            """
            Вычисление площади фигуры.
            Базовый метод возвращает 0, должен быть переопределен в дочерних классах.

            Returns:
                float: площадь фигуры
            """
            return 0.0

        def perimeter(self) -> float:
            """
            Вычисление периметра фигуры.
            Базовый метод возвращает 0, должен быть переопределен в дочерних классах.

            Returns:
                float: периметр фигуры
            """
            return 0.0

        def scale(self, factor: float) -> None:
            """
            Масштабирование фигуры.
            Базовый метод, должен быть переопределен в дочерних классах.

            Args:
                factor: коэффициент масштабирования
            """
            pass

        def __str__(self) -> str:
            """
            Пользовательское строковое представление фигуры.

            Returns:
                str: информативное описание фигуры
            """
            return f"{self._name} (цвет: {self._color})"

        def __repr__(self) -> str:
            """
            Официальное строковое представление фигуры для отладки.

            Returns:
                str: представление для воссоздания объекта
            """
            return f"Shape(color='{self._color}', name='{self._name}', position_x={self._position_x}, position_y={self._position_y})"


    class Rectangle(Shape):
        """
        Класс прямоугольника, наследующийся от Shape.

        Атрибуты:
            _width (float): ширина прямоугольника
            _height (float): высота прямоугольника
        """

        def __init__(self, color: str, width: float, height: float, position_x: float = 0,
                     position_y: float = 0) -> None:
            """
            Инициализация прямоугольника.
            Расширяет конструктор базового класса, добавляя параметры ширины и высоты.

            Args:
                color: цвет прямоугольника
                width: ширина прямоугольника
                height: высота прямоугольника
                position_x: координата X центра
                position_y: координата Y центра
            """
            name = f"Прямоугольник {width} x {height}"
            super().__init__(color, name, position_x, position_y)
            self._width = width
            self._height = height

        def get_dimensions(self) -> tuple[float, float]:
            """
            Получение размеров прямоугольника.

            Returns:
                tuple[float, float]: (ширина, высота)
            """
            return (self._width, self._height)

        def set_dimensions(self, width: float, height: float) -> None:
            """
            Установка размеров прямоугольника.

            Args:
                width: новая ширина
                height: новая высота
            """
            self._width = width
            self._height = height
            self._name = f"Прямоугольник {width} x {height}"

        def area(self) -> float:
            """
            Переопределение метода вычисления площади для прямоугольника.

            Returns:
                float: площадь прямоугольника (ширина * высота)
            """
            return self._width * self._height

        def perimeter(self) -> float:
            """
            Переопределение метода вычисления периметра для прямоугольника.

            Returns:
                float: периметр прямоугольника (2 * (ширина + высота))
            """
            return 2 * (self._width + self._height)

        def scale(self, factor: float) -> None:
            """
            Переопределение метода масштабирования для прямоугольника.

            Причина перегрузки: для прямоугольника масштабирование применяется
            отдельно к ширине и высоте. После масштабирования обновляется название
            для соответствия новым размерам.

            Args:
                factor: коэффициент масштабирования
            """
            self._width *= factor
            self._height *= factor
            self._name = f"Прямоугольник {self._width:.1f} x {self._height:.1f}"

        def __str__(self) -> str:
            """
            Переопределение строкового представления для прямоугольника.

            Returns:
                str: детальное описание прямоугольника
            """
            base_str = super().__str__()
            return f"{base_str}, размеры: {self._width} x {self._height}"

        def __repr__(self) -> str:
            """
            Переопределение официального представления для прямоугольника.

            Returns:
                str: представление для воссоздания объекта Rectangle
            """
            return (f"Rectangle(color='{self._color}', width={self._width}, "
                    f"height={self._height}, position_x={self._position_x}, "
                    f"position_y={self._position_y})")


    class Circle(Shape):
        """
        Класс круга, наследующийся от Shape.

        Атрибуты:
            _radius (float): радиус круга
        """

        def __init__(self, color: str, radius: float, position_x: float = 0, position_y: float = 0) -> None:
            """
            Инициализация круга.
            Расширяет конструктор базового класса, добавляя параметр радиуса.

            Args:
                color: цвет круга
                radius: радиус круга
                position_x: координата X центра
                position_y: координата Y центра
            """
            name = f"Круг r={radius}"
            super().__init__(color, name, position_x, position_y)
            self._radius = radius

        def get_radius(self) -> float:
            """
            Получение радиуса круга.

            Returns:
                float: радиус круга
            """
            return self._radius

        def set_radius(self, radius: float) -> None:
            """
            Установка радиуса круга.

            Args:
                radius: новый радиус
            """
            self._radius = radius
            self._name = f"Круг r={radius}"

        def area(self) -> float:
            """
            Переопределение метода вычисления площади для круга.

            Returns:
                float: площадь круга (π * r²)
            """
            return math.pi * self._radius ** 2

        def perimeter(self) -> float:
            """
            Переопределение метода вычисления длины окружности.

            Returns:
                float: длина окружности (2 * π * r)
            """
            return 2 * math.pi * self._radius

        def scale(self, factor: float) -> None:
            """
            Переопределение метода масштабирования для круга.

            Причина перегрузки: для круга масштабирование применяется к радиусу,
            что приводит к изменению всех геометрических характеристик.
            После масштабирования обновляется название для отображения нового радиуса.

            Args:
                factor: коэффициент масштабирования
            """
            self._radius *= factor
            self._name = f"Круг r={self._radius:.1f}"

        def __str__(self) -> str:
            """
            Переопределение строкового представления для круга.

            Returns:
                str: детальное описание круга
            """
            base_str = super().__str__()
            return f"{base_str}, радиус: {self._radius:.2f}"

        def __repr__(self) -> str:
            """
            Переопределение официального представления для круга.

            Returns:
                str: представление для воссоздания объекта Circle
            """
            return (f"Circle(color='{self._color}', radius={self._radius}, "
                    f"position_x={self._position_x}, position_y={self._position_y})")



    pass
