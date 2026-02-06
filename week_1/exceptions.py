def divide(a: int, b: int):
    try:
        print(a / b)
    except ZeroDivisionError as e:
        print(e)
    except:
        print(e)
    else:
        print("All went good")
    finally:
        print("Just finally block")


divide(1, 0)
divide(1, 1)


class PlatformException(Exception):
    """Unsupported platform"""


try:
    raise PlatformException("Something went wrong")
except PlatformException as p:
    print(p)
