#Write a program to demonstrate instance methods class methods and static methods.
class Student:
    college = "Marwadi University"

    def __init__(self, name):
        self.name = name

    # Instance method
    def show(self):
        print("Student Name:", self.name)

    # Class method
    @classmethod
    def show_college(cls):
        print("College:", cls.college)

    # Static method
    @staticmethod
    def message():
        print("Welcome to Python Programming")

s1 = Student("Divyesh")

s1.show()
Student.show_college()
Student.message()
