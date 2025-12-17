import math
import os

# Display current working directory
print("Current Directory:", os.getcwd())

# List files in current directory
print("Files in directory:", os.listdir())

# Mathematical operations
num = 25
print("Square root:", math.sqrt(num))
print("Factorial of 5:", math.factorial(5))

# Area of a circle
radius = 7
area = math.pi * math.pow(radius, 2)
print("Area of circle:", area)
