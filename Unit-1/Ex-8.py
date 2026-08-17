# 1. IMMUTABLE (Cannot change)
x = "Hi"
print("String ID before:", id(x))

x = x + "!"  # Creates a brand new object
print("String ID after: ", id(x))  # ID changes

print("-" * 30)

# 2. MUTABLE (Can change)
y = [1, 2]
print("List ID before:", id(y))

y.append(3)  # Modifies the same object in place
print("List ID after: ", id(y))  # ID stays exactly the same
