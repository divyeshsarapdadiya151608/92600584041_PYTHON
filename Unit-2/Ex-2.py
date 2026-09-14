# Program to check whether a number is positive, negative or zero
# Taking input from the user
num = float(input("Enter a number: "))

# Using nested conditions
if num >= 0:
    if num == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")
else:
    print("The number is negative.")
