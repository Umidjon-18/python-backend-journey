class Single:

    def __new__(cls):
        if not hasattr(cls, "singleton"):
            cls.singleton = super().__new__(cls)
        return cls.singleton

    def __init__(self):
        self.some = "Something in your eyes"


a = Single()
b = Single()
print(a.some)
print(b.some)

a.some = "Go to my website"
print(a.some)
print(b.some)

print(a is b)
