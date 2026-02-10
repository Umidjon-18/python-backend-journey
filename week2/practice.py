### Level 1 — Core OOP Foundations

# class Person:
#     def __init__(self, name: str, age: str):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         print(f"name: {self.name}, age: {self.age}")

#     def have_birthday(self):
#         pass


# p = Person("John", 24)
# p.introduce()


# class BankAccount:
#     def __init__(self, owner: str, balance: float):
#         self.owner = owner
#         self.__balance = balance

#     def deposit(self, amount: float):
#         self.__balance += amount
#         print(f"Balance updated")

#     def withdraw(self, amount: float):
#         self.__balance -= amount
#         print(f"Balance updated")

#     def get_balance(self):
#         print(f"Your balance: {self.__balance}")


# account = BankAccount("John", 123)

# account.deposit(120)
# account.withdraw(60)
# account.get_balance()


# class Car:
#     def __init__(self, brand: str, fuel: float):
#         self.brand = brand
#         self.fuel = fuel
#         self.__traveled = 0
#         self.__consumption = 10

#     def drive(self, distance: float):
#         self.__traveled += distance
#         self.fuel -= distance / self.__consumption
#         print("Traveled distance updated")

#     def refuel(self, amount: float):
#         self.fuel += amount
#         print("Car refueled")

#     def show_info(self):
#         print(
#             f"car brand: {self.brand}, fuel consumption: {self.__consumption}, fuel remind: {self.fuel}, traveled distance: {self.__traveled}"
#         )


# cr = Car("BMW", 50)
# cr.drive(440)
# cr.refuel(10)
# cr.show_info()


# class Rectangle:
#     def __init__(self, width: float, height: float):
#         if width <= 0 or height <= 0:
#             raise ValueError("Value cannot be negative or 0")
#         self.width = width
#         self.height = height

#     def perimeter(self) -> float:
#         return 2 * (self.width + self.height)

#     def area(self) -> float:
#         return self.width * self.height


# rc = Rectangle(12, 10)
# print(rc.perimeter())
# print(rc.area())


# class Counter:
#     total_counters = 0

#     def __init__(self):
#         Counter.total_counters += 1
#         self.count = 0

#     def increment(self, count=1):
#         if count < 0:
#             raise ValueError("cannot be negative")
#         self.count += count

#     def reset(self):
#         self.count = 0


# c1 = Counter()
# c1.increment()
# print(c1.count)
# c1.reset()
# print(c1.count)
# c2 = Counter()
# c3 = Counter()

# print(f"Total counters: {Counter.total_counters}")


# class SomeInterface:
#     variable = 0

#     @classmethod
#     def change_class_variable(cls):
#         cls.variable += 1

#     @staticmethod
#     def do_something():
#         print("Something is done")


# print(SomeInterface.variable)
# SomeInterface.change_class_variable()
# print(SomeInterface.variable)

# SomeInterface.do_something()


### Level 2 — Inheritance & Polymorphism

from math import *


class Animal:
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print("Wow wow")


class Cat(Animal):
    def make_sound(self):
        print("Meow meow")


d = Dog()
d.make_sound()
c = Cat()
c.make_sound()


class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return pi * self.radius * self.radius


rect = Rectangle(12, 10)
circ = Circle(10)
print(rect.area())
print(circ.area())


class Book:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Book('{self.name}')"


class Library:
    def __init__(self, books: list[Book]):
        self.books = books

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book: Book):
        self.books.remove(book)

    def find_book(self, search: str):
        return [book for book in self.books if search.lower() in book.name.lower()]

    def info(self):
        for book in self.books:
            print(book)

    def __repr__(self):
        return ", ".join(book.name for book in self.books)


b1 = Book("Otamdan qolgan dalalar")
b2 = Book("O'tkan kunlar")
b3 = Book("Mehrobdan chayon")
b4 = Book("Jinoyat va jazo")
b5 = Book("Alkimyogar")
b6 = Book("Bobilning eng boy odami")

lb = Library([b1, b2, b3, b4])

lb.add_book(book=b5)
print(lb.find_book("lar"))
lb.add_book(book=b6)
lb.info()
print(lb)


class SchoolClass:
    def __init__(self, name: str):
        self.name = name

    def __eq__(self, value):
        if not isinstance(value, SchoolClass):
            return NotImplemented
        return self.name == value.name

    def __hash__(self):
        return self.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"SchoolClass('{self.name}')"


class Teacher:
    def __init__(self, name: str):
        self.name = name
        self.classes: list[SchoolClass] = []

    def add_class(self, cl: SchoolClass):
        if cl not in self.classes:
            self.classes.append(cl)

    def remove_class(self, cl: SchoolClass):
        self.classes.remove(cl)


class Student:
    def __init__(self, name: str):
        self.name = name
        self.classes: list[SchoolClass] = []

    def add_class(self, cl: SchoolClass):
        if cl not in self.classes:
            self.classes.append(cl)

    def remove_class(self, cl: SchoolClass):
        self.classes.remove(cl)


class School:
    def __init__(self):
        self._teachers: list[Teacher] = []
        self._students: list[Student] = []
        self._classes: list[SchoolClass] = []

    def add_class(self, cl: SchoolClass):
        if cl not in self._classes:
            self._classes.append(cl)

    def add_teacher(self, teacher: Teacher):
        self._teachers.append(teacher)

    def add_student(self, student: Student):
        self._students.append(student)

    def remove_teacher(self, teacher: Teacher):
        self._teachers.remove(teacher)

    def remove_student(self, student: Student):
        self._students.remove(student)


### Level 4 — Encapsulation, Properties, Validation


class User:
    def __init__(self, password: str):
        password = password.strip()
        if len(password) < 8:
            raise ValueError("Minimum password length is 8")
        self.__password = password

    def check_password(self, p: str) -> bool:
        return self.__password == p


us = User("securepassword#")

print(us.check_password("somepassword"))


class Temperature:
    def __init__(self, temperature: float):
        if temperature < -273.15:
            raise ValueError("Given value is smaller than absolut zero")
        self.__temperature = temperature

    @property
    def celsius(self):
        return self.__temperature

    @property
    def fahrenheit(self):
        return self.__temperature * 9 / 5 + 32

    @property
    def kelvin(self):
        return self.__temperature + 273.15


tm = Temperature(12)
print(tm.fahrenheit)
print(tm.kelvin)


class Product:
    def __init__(self, id: int, name: str, price: float):
        if id < 0:
            raise ValueError("Id cannot be negative")
        if price <= 0:
            raise ValueError("Price is invalid")
        self.__id = id
        self.name = name
        self.__price = price

    @property
    def price(self):
        return self.__price

    @property
    def id(self):
        return self.__id


pr = Product(1, "Apple", 12000)
print(pr.id)


class Timer:
    def __init__(self, time: int):
        if time < 0:
            raise ValueError("time must not be negative")
        self.__time = time

    @property
    def time(self):
        return self.__time

    def tick(self, value: int):
        if value < 0:
            raise ValueError("Tick value cannot be negative")
        self.__time += value


class Wallet:
    def __init__(self, balance: float):
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def spend(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if self.__balance < amount:
            raise ValueError("Balance is less than amount")
        self.__balance -= amount


### Level 5 — Magic Methods & Pythonic OOP


class Something:
    def __init__(self, value: float):
        self.value = value

    def __add__(self, other):
        if not isinstance(other, Something):
            return NotImplemented
        return Something(self.value + other.value)

    def __len__(self):
        return self.value

    def __eq__(self, other):
        if not isinstance(other, Something):
            return NotImplemented
        return self.value == other.value

    def __gt__(self, other):
        if not isinstance(other, Something):
            return NotImplemented
        return self.value > other.value

    def __lt__(self, other):
        if not isinstance(other, Something):
            return NotImplemented
        return self.value < other.value

    def __str__(self):
        return f"Something({self.value})"


sm = Something(12)
sm2 = Something(24)

print(sm > sm2)


class CustomRange:
    def __init__(self, start: int, stop: int, step: int = 1):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if (self.step > 0 and self.current >= self.stop) or (
            self.step < 0 and self.current <= self.stop
        ):
            raise StopIteration
        value = self.current
        self.current += self.step
        return value


for i in CustomRange(1, 10, 1):
    print(i)

from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

    @property
    @abstractmethod
    def balance(self):
        pass


class CardPayment(Payment):
    def __init__(self, balance: float):
        self.__balance = balance

    def pay(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficent amount")
        self.__balance -= amount

    @property
    def balance(self):
        return self.__balance


class CashPayment(Payment):
    def __init__(self, balance: float):
        self.__balance = balance

    def pay(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficent amount")
        self.__balance -= amount

    @property
    def balance(self):
        return self.__balance


crp = CardPayment(1000)
crp.pay(500)
print(crp.balance)
