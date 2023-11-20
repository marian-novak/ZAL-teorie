from math import isclose
from math import sqrt

od = int(input("Zadejte M: "))
do = int(input("Zadejte N: "))

cislo = od

while cislo <= do:   
   if cislo > 1:
      i = 2
      yesprvo = True
      while i <= sqrt(cislo):
           if cislo % i == 0:
               yesprvo = False
               break
           
           i = i + 1
           if yesprvo == True:
                    print(cislo)
cislo = cislo + 1