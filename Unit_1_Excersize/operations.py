x = 15
y = 4
a = True
b = False

# -------------------------------------------------------------
# ARITHMETIC OPERATIONS
# -------------------------------------------------------------
print("=== Arithmetic Operations ===")
print(f"Addition ({x} + {y}):", x + y)          
print(f"Subtraction ({x} - {y}):", x - y)       
print(f"Multiplication ({x} * {y}):", x * y)    
print(f"Float Division ({x} / {y}):", x / y)    
print(f"Floor Division ({x} // {y}):", x // y)
print(f"Modulus ({x} % {y}):", x % y)       
print(f"Exponentiation ({x} ** {y}):", x ** y)  

# -------------------------------------------------------------
# RELATIONAL (COMPARISON) OPERATIONS
# -------------------------------------------------------------
print("\n=== Relational Operations ===")
print(f"Greater Than ({x} > {y}):", x > y)
print(f"Less Than ({x} < {y}):", x < y)
print(f"Equal To ({x} == {y}):", x == y)
print(f"Not Equal To ({x} != {y}):", x != y)
print(f"Greater Than or Equal To ({x} >= {y}):", x >= y)
print(f"Less Than or Equal To ({x} <= {y}):", x <= y)

# -------------------------------------------------------------
# LOGICAL OPERATIONS
# -------------------------------------------------------------
print("\n=== Logical Operations ===")
# Returns True only if both conditions are True
print(f"Logical AND ({x} > {y} and {a}):", (x > y) and a) 
# Returns True if at least one condition is True
print(f"Logical OR ({x} < {y} or {b}):", (x < y) or b)   
# Reverses the boolean value
print(f"Logical NOT (not {a}):", not a)                  
