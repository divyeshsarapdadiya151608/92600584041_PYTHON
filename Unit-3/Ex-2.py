# Method 1: Import complete module
import math

print("Square root:", math.sqrt(25))


# Method 2: Import specific function
from math import factorial

print("Factorial:", factorial(5))


# Method 3: Import module with alias
import math as m

print("Power:", m.pow(2, 3))


# Method 4: Import multiple functions
from math import ceil, floor

print("Ceiling:", ceil(4.3))
print("Floor:", floor(4.8))
