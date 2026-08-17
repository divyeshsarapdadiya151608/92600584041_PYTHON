# Tuple example
t = (1, 2, 3, 2, 4)
print("Tuple:", t)
print("First:", t[0], "Last:", t[-1])
print("Slice:", t[1:4])
print("Count of 2:", t.count(2))
print("Index of 4:", t.index(4))

# Set example
s = {1, 2, 3, 2, 4}
print("\nSet:", s)
s.add(5)
print("After add:", s)
s.discard(3)
print("After discard:", s)

a, b = {1, 2, 3}, {3, 4, 5}
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
print("SymDiff:", a ^ b)
