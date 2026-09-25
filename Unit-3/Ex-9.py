#Write a program to use re module functions such as match search and findall.
import re

text = "Python is easy. Python is powerful. Python is popular."

# Using match()
result1 = re.match("Python", text)

if result1:
    print("match():", result1.group())
else:
    print("match(): Pattern not found")


# Using search()
result2 = re.search("powerful", text)

if result2:
    print("search():", result2.group())
else:
    print("search(): Pattern not found")


# Using findall()
result3 = re.findall("Python", text)

print("findall():", result3)
