import asyncio


def get_info(name: str, age: int, height: float):
    print(f"name: {name}, age: {age}, height: {height}")


if __name__ == "__main__":
    get_info("asas", 45, height=1231)


def just(*args: list[int]):
    print(args[0])


if __name__ == "__main__":
    just(1, 2, 3, 4, 5, 5)


def kjust(**kargs):
    print(kargs["first"])


if __name__ == "__main__":
    kjust(first="Umidjon")


def pos_arg(a, b, /, k):
    print(a)
    print(b)
    print(k)


if __name__ == "__main__":
    pos_arg(12, "23", k=45)


def unpacked(*args):
    print(args[0])
    print(args[1])
    print(args[2])


if __name__ == "__main__":
    unpacked(*[12, 23, 34])


def function(one, two, three):
    print(f"{one = }")
    print(f"{two = }")
    print(f"{three = }")


numbers = {"one": 1, "two": 2, "three": 3}
if __name__ == "__main__":
    function(**numbers)
one = 1
two = 2
three = 3


def fun(a: int | str):
    print(a)


if __name__ == "__main__":
    fun(12)
    fun("as")
    fun(True)


async def fun():
    await asyncio.sleep(1)
    return 12


if __name__ == "__main__":
    print(asyncio.run(fun()))
