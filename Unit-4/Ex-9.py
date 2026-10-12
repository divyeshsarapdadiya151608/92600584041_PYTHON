
# Writing data using write mode
f = open("student.txt", "w")
f.write("Welcome to Python\n")
f.write("File Handling Example\n")
f.close()

# Reading data using read mode
f = open("student.txt", "r")
print("Reading file:")
print(f.read())
f.close()

# Appending data using append mode
f = open("student.txt", "a")
f.write("New line added\n")
f.close()

# Reading updated data
f = open("student.txt", "r")
print("Updated file:")
print(f.read())
f.close()

# Using exclusive creation mode
try:
    f = open("newfile.txt", "x")
    f.write("New file created")
    f.close()
    print("File created successfully")
except FileExistsError:
    print("File already exists")