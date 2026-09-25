#Write a program to copy move and delete files using shutil module.
import shutil
import os

# Create a source file
with open("source.txt", "w") as file:
    file.write("This is a sample file for shutil operations.")

print("Source file created.")

# Copy the file
shutil.copy("source.txt", "copy.txt")
print("File copied successfully.")

# Move the copied file
shutil.move("copy.txt", "moved.txt")
print("File moved successfully.")

# Delete the moved file
os.remove("moved.txt")
print("File deleted successfully.")
