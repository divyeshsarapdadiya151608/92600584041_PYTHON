# Program to demonstrate iterators and iterables
# Creating an iterable
numbers = [10, 20, 30, 40, 50]

print("Iterable:", numbers)

# Creating an iterator
iterator = iter(numbers)

# Accessing elements using next()
print("\nIterator elements:")
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
