#recursion using factorial
def factorial(num): 
    if (num==1 or num==0):
        return 1
    else:
        return (num * factorial(num - 1)) 
num = int(input("Enter a number: "));
print("number : ",num)
print("Factorial : ",factorial(num))

#recursion using fibonacci series
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
      
n_terms = int(input("Enter a number: "));
for i in range(n_terms):
    print(fibonacci(i), end=" ")
