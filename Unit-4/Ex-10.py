#10.Write a program to perform file pointer operations using seek and tell methods.
# Creating a file
with open("sample.txt", "w") as f:
    f.write("Hello Python Programming")

# Performing file pointer operations
with open("sample.txt", "r") as f:
    print("Initial position:", f.tell())

    data = f.read(5)
    print("Data read:", data)
    print("Position after reading:", f.tell())

    f.seek(0)
    print("Position after seek(0):", f.tell())

    data = f.read(5)
    print("Data read again:", data)

    f.seek(6)
    print("Position after seek(6):", f.tell())
    print("Remaining data:", f.read())