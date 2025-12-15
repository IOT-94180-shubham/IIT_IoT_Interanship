# Program to explore string slicing

s = input("Enter a string: ")

print("\nOriginal String:", s)

# Basic slicing
print("s[0:5] :", s[0:5])
print("s[2:7] :", s[2:7])

# Slicing from start
print("s[:5]  :", s[:5])

# Slicing till end
print("s[3:]  :", s[3:])

# Negative indexing
print("s[-5:] :", s[-5:])
print("s[:-3] :", s[:-3])

# Step slicing
print("s[::2] :", s[::2])

# Reverse string
print("s[::-1]:", s[::-1])
