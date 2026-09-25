#Write a program to perform file and directory operations using os and sys modules.
import os
import sys

# Display current working directory
print("Current Directory:")
print(os.getcwd())

# Create a directory
folder = "MyFolder"

if not os.path.exists(folder):
    os.mkdir(folder)
    print("Directory created successfully.")
else:
    print("Directory already exists.")

# Display files and directories
print("\nDirectory Contents:")
print(os.listdir())

# Display Python version
print("\nPython Version:")
print(sys.version)

# Display command-line arguments
print("\nCommand-line Arguments:")
print(sys.argv)
