from typing import Optional

### Square and Cubes

# max = int(input("Input max number: "))
# dictionary = {}
# for n in range(1, max + 1):
#     dictionary[n] = n * n * n

# print(dictionary)


### Password level checking

# password = input("Enter password: ")


# def check(password: str) -> None:
#     if len(password) < 4 or not has_letter(password):
#         print("Weak")
#         return
#     if has_number(password) and has_special_character(password):
#         print("Strong")
#     else:
#         print("Medium")


# def has_special_character(string: str) -> bool:
#     specials = ("@", "$", "%", "#")
#     return any(s in string for s in specials)


# def has_number(string: str) -> bool:
#     return any(char.isdigit() for char in string)


# def has_letter(string: str) -> bool:
#     return any(char.isalpha() for char in string)


# check(password)


### Keyword Argument Logger
# def logger(*args, **kargs):
#     for arg in args:
#         print(arg)
#     for key in kargs:
#         print(f"{key}: {kargs[key]}")


# logger(1, 2, 3, 4, 5, 6, 7, a=12, b=23)


### Calculator with Safe Division

# def add(a: float, b: float) -> float:
#     return a + b


# def subtract(a: float, b: float) -> float:
#     return a - b


# def multiply(a: float, b: float) -> float:
#     return a * b


# def divide(a: float, b: float) -> Optional[float]:
#     if b == 0:
#         return None

#     return a / b


# print(add(1, 2))
# print(subtract(1, 2))
# print(multiply(1, 2))
# print(divide(1, 2))
# print(divide(1, 0))


### Custom File Reader
# class FileEmptyError(Exception):
#     pass


# try:
#     with open("../example.txt") as file:
#         content = file.read()
#         if not content:
#             raise FileEmptyError("Bu fayl bo'sh")
#         print(content)
# except FileEmptyError as e:
#     print(e)
# except FileNotFoundError:
#     print("Fayl topilmadi")

### Simple Config Loader

# try:
#     dict = {}
#     with open("../example.txt") as file:
#         for line in file.readlines():
#             if not line or line.startswith("#"):
#                 continue
#             if "=" not in line:
#                 continue
#             key, value = line.split("=", maxsplit=1)
#             if key:
#                 dict[key.strip()] = value.strip()

#         print(dict)
# except FileNotFoundError as e:
#     print(e)

# from functions import *

# get_info("Bob", 12, 150)

### Word Frequency Counter

# import string

# paragraph = input("Enter text: ")


# def count_word_frequency(text: str) -> dict:
#     text = text.lower().translate(str.maketrans("", "", string.punctuation))
#     counted = {}
#     for word in text.split():
#         counted[word] = counted.get(word, 0) + 1

#     return counted


# print(count_word_frequency(paragraph))

### Email Validator

# email = input('Enter email: ')

# def validate_email(email: str)-> bool:
#     if '@' not in email:
#         return False
    
