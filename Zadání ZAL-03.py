from math import sqrt

od = int(input("Zadejte N: "))
do = int(input("Zadejte M: "))

while od <= do:
    if od >= 2:
        je_prvocislo = True
        i = 2
        while i <= sqrt(od):
            if od % i == 0:
                je_prvocislo = False
                break
            i = i + 1
        if je_prvocislo:
            print(od)
    od = od + 1