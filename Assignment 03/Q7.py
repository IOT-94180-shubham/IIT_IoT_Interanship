# Recursive function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Recursive function to calculate power
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)


# Main program
num = int(input("Enter a number to find factorial: "))
print(f"Factorial of {num} is {factorial(num)}")

base = int(input("\nEnter base for power calculation: "))
exp = int(input("Enter exponent: "))
print(f"{base}^{exp} = {power(base, exp)}")
