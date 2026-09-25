#Write a program to demonstrate basic regular expression pattern matching.
import re

text = "My phone number is 9876543210"

# Pattern for a 10-digit phone number
pattern = r"\d{10}"

# Search for the pattern
result = re.search(pattern, text)

if result:
    print("Pattern found:", result.group())
else:
    print("Pattern not found.")
