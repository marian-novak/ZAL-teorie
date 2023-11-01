from math import sqrt
from math import fabs
print("Zadejte parametry kruznice #1: ")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
r1 = float(input("r1: "))

print("Zadejte parametry kruznice #2: ")
x2 = float(input("x2: "))
y2 = float(input("y2: "))
r2 = float(input("r2: "))

vzdalenostx = fabs(x1 - x2)
vzdalenosty = fabs(y1 - y2)
vzdalenost = sqrt(vzdalenostx**2 + vzdalenosty**2)

if x1==x2 and y1==y2 and r1==r2:
    print("Kruznice splyvaji")

if vzdalenost < r1 - r2:
    print("Kruznice #2 lezi uvnitr kruznice #1")

if vzdalenost < r2 - r1:
   print("Kruznice #1 lezi uvnitr kruznice #2")

if vzdalenost == r1 + r2:
    print("Kruznice lezi vne sebe")

if vzdalenost < r1 + r2:
    print("Kruznice se protinaji")

if vzdalenost == r1 + r2:
    print("Vnejsi dotyk")
