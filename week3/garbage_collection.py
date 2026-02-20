import sys

x = [1, 2, 3]
print(sys.getrefcount(x))
y = x
print(sys.getrefcount(x))
y = None
print(sys.getrefcount(x))
