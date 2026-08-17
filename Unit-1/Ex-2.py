# 1. Basic Data Types
my_int = 10
my_float = 5.5
my_str = "20"

print(type(my_int))    # Outputs: <class 'int'>
print(type(my_float))  # Outputs: <class 'float'>
print(type(my_str))    # Outputs: <class 'str'>

# 2. Implicit Casting (Automatic)
result = my_int + my_float
print(result)          # Outputs: 15.5 (Converted to float automatically)

# 3. Explicit Casting (Manual)
new_int = int(my_float)
new_str = str(my_int)
new_float = float(my_str)

print(new_int)         # Outputs: 5 (Drops the decimal)
print(new_str)         # Outputs: "10" (Becomes text)
print(new_float)       # Outputs: 20.0 (Becomes a decimal)
