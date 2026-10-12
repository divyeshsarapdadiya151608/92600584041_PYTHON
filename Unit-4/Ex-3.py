#Write a program to illustrate instance variables and class variables.
class Student:
    college = "Marwadi University"  # Class variable

    def __init__(self, name, roll_no):
        self.name = name        # Instance variable
        self.roll_no = roll_no  # Instance variable

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("College:", Student.college)

s1 = Student("Divyesh", 1)
s2 = Student("Rahul", 2)

s1.display()
print()
s2.display()
