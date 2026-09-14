# Program to demonstrate conditional statements
# Using if statement
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")


# Using if-else statement
number = int(input("\nEnter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# Using if-elif-else statement
marks = int(input("\nEnter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")
