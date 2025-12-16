# List of lambda conversion functions (step-by-step)
converters = [
    ("kg",  lambda tonnes: tonnes * 1000),        # tonnes → kilograms
    ("gm",  lambda kg: kg * 1000),                 # kilograms → grams
    ("mg",  lambda gm: gm * 1000),                 # grams → milligrams
    ("lbs", lambda mg: mg / 453592.37)             # milligrams → pounds
]

# Input from user (in tonnes)
weight = float(input("Enter weight in tonnes: "))

# Apply conversions sequentially
current = weight
print("\nConverted Weights:")

for unit, func in converters:
    current = func(current)
    print(f"{current} {unit}")
