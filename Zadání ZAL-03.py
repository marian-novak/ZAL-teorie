from math import isclose

od = int(input("Zadejte M: "))
do = int(input("Zadejte N: "))

jeprvo = True
while od >= 0:
    if (od % 2 != 0) and (od % 3 != 0) and (od % 5 != 0) and (od % 7 != 0) and od != 1:
        print(od)
    if od == 2:
        print(od)
    if od == 3:
        print(od)
    if od == 5:
        print(od)
    if od == 7:
        print(od)
    od = od + 1
    if od > do:
        break