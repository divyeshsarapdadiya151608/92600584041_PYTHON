# Program to iterate over lists, strings and dictionaries
# Iterating over a list
print("List elements:")
numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(num)


# Iterating over a string
print("\nString characters:")
name = "Python"

for char in name:
    print(char)


# Iterating over a dictionary
print("\nDictionary elements:")
student = {
    "Name": "Divyesh",
    "Age": 22,
    "Course": "MCA"
}

for key, value in student.items():
    print(key, ":", value)
