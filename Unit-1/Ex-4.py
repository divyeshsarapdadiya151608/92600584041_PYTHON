text = "Python Programming"

# 1. Slicing
print(text[0:6])    # Prints: Python (First 6 letters)
print(text[:3])     # Prints: Pyt    (First 3 letters)
print(text[7:])     # Prints: Programming (From index 7 to the end)

# 2. Formatting 
name = "Alice"
age = 25
print(f"Hello, my name is {name} and I am {age} years old.")

# 3. Built-in Functions 
print(text.upper())      # Prints: PYTHON PROGRAMMING
print(text.lower())      # Prints: python programming
print(text.replace("Python", "Java"))  # Prints: Java Programming
print(len(text))         # Prints: 18 (Total character count)
