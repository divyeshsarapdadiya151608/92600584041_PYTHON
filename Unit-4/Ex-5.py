#Write a program to implement single multilevel and multiple inheritance.

# Single inheritance
class A:
    def show_a(self):
        print("Class A")

class B(A):
    def show_b(self):
        print("Class B")

obj1 = B()
obj1.show_a()
obj1.show_b()

# Multilevel inheritance
class C(B):
    def show_c(self):
        print("Class C")

obj2 = C()
obj2.show_a()
obj2.show_b()
obj2.show_c()

# Multiple inheritance
class X:
    def show_x(self):
        print("Class X")

class Y:
    def show_y(self):
        print("Class Y")

class Z(X, Y):
    pass

obj3 = Z()
obj3.show_x()
obj3.show_y()
