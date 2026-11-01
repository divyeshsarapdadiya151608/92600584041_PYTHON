# Write a program to demonstrate different types of errors and exceptions in Python.

# Syntax Error
# print("Hello")

# Name Error
try:
    print(x)
except NameError as e:
    print("Name Error:", e)

# Type Error
try:
    result = "Hello" + 10
except TypeError as e:
    print("Type Error:", e)

# Value Error
try:
    num = int("abc")
except ValueError as e:
    print("Value Error:", e)

# Zero Division Error
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Zero Division Error:", e)

# Index Error
try:
    numbers = [10, 20, 30]
    print(numbers[5])
except IndexError as e:
    print("Index Error:", e)

# Key Error
try:
    student = {"name": "Rahul"}
    print(student["age"])
except KeyError as e:
    print("Key Error:", e)
