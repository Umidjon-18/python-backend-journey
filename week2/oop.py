class Parent:
    class_attribute = "Hello"

    def go(self):
        print(self.class_attribute)


class Child(Parent):
    class_attribute = "Good bye"


p = Parent()
p2 = Parent()

ch = Child()

p.class_attribute = "Something"

print(p.class_attribute)
print(p2.class_attribute)
print(ch.class_attribute)
p2.go()

print(isinstance(ch, Parent))