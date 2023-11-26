from math import sqrt

od = int(input("Zadejte N: "))
do = int(input("Zadejte M: "))

cislo = od
while cislo <= do:
    if cislo >= 2:
        je_prvocislo = True
        i = 2
        while i <= sqrt(cislo):
            if cislo % i == 0:
                je_prvocislo = False
                break
            i = i + 1
        if je_prvocislo:
            print(cislo)
    cislo = cislo + 1