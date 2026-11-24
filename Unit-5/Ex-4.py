# 4. Demonstrate the use of the assert statement.
# Program to demonstrate assert statement
num = int(input("Enter a positive number: "))

try:
    assert num > 0, "Number must be positive."
    print("Valid number:", num)
except AssertionError as e:
    print("Assertion Error:", e)
