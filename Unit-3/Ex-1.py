#Write a program to create and import a user-defined module. 

#mymodule.py
def greet(name):
    print("Hello", name)

def add(a, b):
    return a + b

#main.py
import mymodule

mymodule.greet("World!")

result = mymodule.add(10, 20)
print("Addition =", result)
