class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self._age = age

p = Person("John", 24)
print(p.name)
print(p._age)
