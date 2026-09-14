# Program to generate a sequence of numbers using generator
# Generator function
def generate_numbers(n):
    for i in range(1, n + 1):
        yield i

# Taking input from the user
num = int(input("Enter the number: "))

# Calling the generator function
print("Generated sequence:")

for value in generate_numbers(num):
    print(value)
