# Method 1: Using loop (simple & exam-friendly)
def overlapping(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False


# Method 2: Using set (efficient)
def overlapping_set(list1, list2):
    return bool(set(list1) & set(list2))


# Example
a = [1, 2, 3, 4]
b = [5, 6, 3, 8]

print("Using loop method:", overlapping(a, b))
print("Using set method :", overlapping_set(a, b))
