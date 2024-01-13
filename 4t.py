import math

a = float(input("Enter a number: "))
b = float(input("Enter a number: "))
if a < 0.0 or b < 0.0:
    print("Error")
else:
    print("Geometric mean = ", math.sqrt(a*b))