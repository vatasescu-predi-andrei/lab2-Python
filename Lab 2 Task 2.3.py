#task2.3
from math import sqrt
a=float(input("Enter the length of side a:"))
b=float(input("Enter the length of side b:"))
h= sqrt(a**2 + b**2)
newh=round(h, 2)
print("The length of the hypotenuse is", newh)
