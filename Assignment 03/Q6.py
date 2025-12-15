# Functions for basic arithmetic operations

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero"
    return a / b


# Function that takes another function as argument
def calculate(operand1, operand2, operation):
    return operation(operand1, operand2)


# Testing calculate() with different inputs
print("Addition:", calculate(10, 5, add))
print("Subtraction:", calculate(10, 5, subtract))
print("Multiplication:", calculate(10, 5, multiply))
print("Division:", calculate(10, 5, divide))

print("\nDifferent set of inputs:")
print("Addition:", calculate(25, 15, add))
print("Multiplication:", calculate(6, 4, multiply))
print("Division:", calculate(20, 0, divide))

