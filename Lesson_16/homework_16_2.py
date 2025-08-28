from abc import ABC, abstractmethod
import math


class Figure(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Прямокутник
class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Коло
class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Трикутник
class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        # Формула Герона
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


# Квадрат
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


# Ромб (за стороною та кутом у градусах)
class Rhombus(Figure):
    def __init__(self, side, angle_deg):
        self.side = side
        self.angle = math.radians(angle_deg) # переводимо в радіани

    def area(self):
        return self.side ** 2 * math.sin(self.angle)

    def perimeter(self):
        return 4 * self.side


#Тестуємо
figures = [
    Rectangle(15, 20),
    Circle(5),
    Triangle(10, 10, 15),
    Square(6),
    Rhombus(7, 60)
]

for f in figures:
    print(f"{f.__class__.__name__}:")
    print(f" Площа = {f.area():.2f}")
    print(f" Периметр = {f.perimeter():.2f}")
    print()

