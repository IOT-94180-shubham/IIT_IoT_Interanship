from Q3geometry import area_circle, area_rectangle

# User input
r = float(input("Enter radius of circle: "))
l = float(input("Enter length of rectangle: "))
b = float(input("Enter breadth of rectangle: "))

# Calculations
print("Area of Circle:", area_circle(r))
print("Area of Rectangle:", area_rectangle(l, b))
