from math import sqrt

od = int(input("Zadejte N: "))
do = int(input("Zadejte M: "))

while od <= do:
    if od >= 2:
        je_prvocislo = True
        delitel = 2
        while delitel <= sqrt(od):
            if od % delitel == 0:
                je_prvocislo = False
                break
            delitel = delitel + 1
        if je_prvocislo:
            print(od)
    od = od + 1