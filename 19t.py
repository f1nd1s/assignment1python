import math

x = float(input("Enter a number: "))
y = float(input("Enter a number: "))
z = float(input("Enter a number: "))
a = (math.sqrt(abs(x-1)) - abs(y)*(1/3)) / (1 + ((x**2)/2) + ((y**2)/4))
b = x * (math.atan(z) + math.e**(-(x+3)))
print("a is ", a)
print("b is ", b)