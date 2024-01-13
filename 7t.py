A = float(input("Enter a number: "))
B = float(input("Enter a number: "))
C = float(input("Enter a number: "))
temp = A
A = C
C = B
B = temp
print("The new value of A is ", A)
print("The new value of B is ", B)
print("The new value of C is ", C)