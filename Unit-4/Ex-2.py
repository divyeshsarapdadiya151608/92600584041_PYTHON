#Write a program to demonstrate constructor and destructor usage.
class Student:
    def __init__(self):
        print("Constructor called")

    def __del__(self):
        print("Destructor called")

# Creating an object
s1 = Student()

# Deleting the object
del s1
