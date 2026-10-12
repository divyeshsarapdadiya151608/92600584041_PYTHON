
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass

obj = D()

# Demonstrating MRO
print("Method Resolution Order:")
print([cls.__name__ for cls in D.mro()])

obj.show()

# Demonstrating magic methods
class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Student Name: " + self.name

s1 = Student("Divyesh")
print(s1)