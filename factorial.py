def factorial(t):
    if t < 0:
        return None
    fact = 1
    for i in range(1, t + 1):
        fact *= i
    return fact
x = int(input("Enter a positive integer: "))
result = factorial(x)
if result is None:
    print("Enter a positive integer")
else:
    print(f"The factorial of {x} is {result}")
  
