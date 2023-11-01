from math import sqrt
a = float(input("Zadej delku strany a: "))
b = float(input("Zadej delku strany b: "))
c = float(input("Zadej delku strany c: "))


if a > b:
    doc = b
    b = a
    a = doc

if b > c:
    doc = c
    c = b
    b = doc

cprav = sqrt(a*a+b*b)

if c == cprav: 
    print("Trojuhelnik je pravouhly")
else: 
    print("Trojuhelnik neni pravouhly")






#print("Strana c je dlouha: ", sqrt(a*a+b*b))
#int - celé číslo (bez desetin)
#float - číslo s plovoucí řádovou čárkou (s desetinami)
#string - text