from math import sqrt
from math import fabs
print("Zadej prvni bod")
x1 = float(input("x: "))
y1 = float(input("y: "))

print("Zadej druhy bod")
x2 = float(input("x: "))
y2 = float(input("y: "))

print("Souradnice prvniho bodu jsou", x1, y1)
print("Souradnice prvniho bodu jsou", x2, y2)

#if (x1 < x2):
    #a = x2-x1
#else:
    #a = x1-x2
#if (y1 < y2):
    #b = y2-y1
#else:
    #b = y1-y2
a = fabs(x1 - x2)
b = fabs(y1 - y2)
c = sqrt(a**2 + b**2)
print("Vzdalenost mezi body je:", c)