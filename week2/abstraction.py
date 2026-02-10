from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def __init__(self, radius: int):
        self.radius = radius

    def draw(self):
        return f"Circle with radius={self.radius}"


c = Circle(12)
print(c.draw())


class Animal(ABC):
    @property
    @abstractmethod
    def name(self):
        pass


class Dog(Animal):

    @property
    def name(self):
        return "Boyka"


d = Dog()
print(d.name)


class MyClass:

    def __init__(self, name: str):
        self.name = name

    def display(self) -> None:
        print("Hello world")

    def __eq__(self, value):
        return self.name == value


my1 = MyClass("Bob")
my2 = MyClass("Bob")
print(my1 == my2)
