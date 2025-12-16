# Procedure to print histogram
def histogram(numbers):
    for value in numbers:
        print('*' * value)


# Example
print("Histogram for example list [4, 9, 7]:")
histogram([4, 9, 7])

# User input
n = int(input("\nEnter number of elements: "))
data = []

for i in range(n):
    data.append(int(input(f"Enter value {i+1}: ")))

print("\nHistogram for user input:")
histogram(data)
