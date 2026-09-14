# Program to demonstrate break, continue and pass statements
# Using break statement
print("Using break:")
for i in range(1, 6):
    if i == 4:
        break
    print(i)


# Using continue statement
print("\nUsing continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# Using pass statement
print("\nUsing pass:")
for i in range(1, 6):
    if i == 3:
        pass
    print(i)
