# Program to demonstrate list, dictionary and set comprehensions
# List comprehension
numbers = [1, 2, 3, 4, 5]
squares = [num * num for num in numbers]
print("List comprehension:", squares)


# Dictionary comprehension
dictionary = {num: num * num for num in numbers}
print("Dictionary comprehension:", dictionary)


# Set comprehension
sets = {num * num for num in numbers}
print("Set comprehension:", sets)
