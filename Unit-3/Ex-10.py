#Write a program to extract specific information from a text file using regular expressions.
#data.txt
Name: Rahul
Email: rahul@gmail.com
Phone: 9876543210

Name: Divyesh
Email: divyesh@gmail.com
Phone: 9123456780

#extract_information.py
import re

# Open and read the text file
with open("data.txt", "r") as file:
    text = file.read()

# Extract names
names = re.findall(r"Name:\s*(\w+)", text)

# Extract email addresses
emails = re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)

# Extract 10-digit phone numbers
phones = re.findall(r"\b\d{10}\b", text)

# Display extracted information
print("Names:")
print(names)

print("\nEmail Addresses:")
print(emails)

print("\nPhone Numbers:")
print(phones)
