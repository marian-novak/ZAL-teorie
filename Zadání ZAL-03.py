from math import isclose
from math import sqrt

cislo1 = int(input("Zadejte M: "))
cislo2 = int(input("Zadejte N: "))

while cislo1 <= cislo2:
    if cislo1 > 1:
        i = 2
        yesprvo = True
        while i <= cislo2 - 1:
            if cislo1 % i == 0:
                yesprvo = False
                break
            