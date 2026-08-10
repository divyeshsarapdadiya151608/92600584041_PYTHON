# 1. No arguments, no return value
def greet():
    print("Hello! This is a function with no arguments and no return value.")

# 2. Arguments, no return value
def print_sum(a, b):
    print(f"Sum of {a} and {b} is: {a + b}")

# 3. No arguments, return value
def get_number():
    try:
        num = int(input("Enter a number: "))
        return num
    except ValueError:
        print("Invalid input. Returning 0.")
        return 0

# 4. Arguments, return value
def multiply(x, y):
    return x * y

# Main program
if __name__ == "__main__":
    # Example 1: No arguments, no return value
    greet()

    # Example 2: Arguments, no return value
    print_sum(5, 7)

    # Example 3: No arguments, return value
    number = get_number()
    print(f"You entered: {number}")

    # Example 4: Arguments, return value
    result = multiply(number, 10)
    print(f"{number} multiplied by 10 is: {result}")

