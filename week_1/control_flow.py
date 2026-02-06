# result = True

# if result:
#     print("Yeah, we did it")
# else:
#     print("Ooops, something went wrong")


# def get_result(target: int):
#     return 0 if target < 0 else target


# print(get_result(1))
# print(get_result(-1))

# values = {"a": 2, "b": 4}
# for [key, value] in values.items():
#     print(key, value)


# values = {"a", "b", "c"}
# for value in values:
#     print(value)

# for char in "abcdefg":
#     print(char)

# user_input = ""
# while user_input != "exit":
#     user_input = input("Type something: ")
#     print(f"You typed: {user_input}")
# else:
#     print("As you typed 'exit', the program quit")

# emails = [
#     " alice@example.org ",
#     "BOB@example.com",
#     "charlie@EXAMPLE.com",
#     "David@example.net",
#     " bob@example.com",
#     "JohnDoe@example.com",
#     "DAVID@Example.net",
# ]

# lowered_emails = [email.strip().lower() for email in emails if "@" in email]
# print(lowered_emails)


# def count_down(number: int):
#     if number <= 0:
#         print("End")
#     else:
#         print(number)
#         count_down(number - 1)


# count_down(9)

# if isinstance(1, int):
#     print("Integer")

# with open("example.txt", mode="a", encoding="utf-8") as file:
#     file.write("Bismillahir Rohmanir Rohiym\n")


try:
    print(12)
except:
    print(f"Something went wrong")
else:
    print("Else block worked")
finally:
    print("Finally block worked")
