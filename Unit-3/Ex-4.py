#Write a program to generate random numbers using random module.
import random

# Generate a random integer
print("Random number:", random.randint(1, 100))

# Generate a random decimal number
print("Random decimal:", random.random())

# Select a random item from a list
numbers = [10, 20, 30, 40, 50]

print("Random choice:", random.choice(numbers))

# Shuffle the list
random.shuffle(numbers)

print("Shuffled list:", numbers)
