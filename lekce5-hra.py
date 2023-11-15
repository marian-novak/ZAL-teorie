import random

#a = int(input("První číslo: "))
#b = int(input("Druhé číslo: "))

cislo = random.randint(0, 99)

print("Myslím si cislo mezi 0 a 99, hadej jake to je.")

odpoved = -1
pokusu = 0

while odpoved != cislo:
    odpoved = int(input("Hadej cislo: "))
    pokusu = pokusu + 1
    if (odpoved == cislo) and pokusu < 7:
        print("Spravne!")
        print("A zabralo ti to jen", pokusu, "pokusu ")
    if (odpoved == cislo) and pokusu >= 7:
        print("Jses kkt? Zabralo ti to", pokusu, "pokusu ty magore!")
    elif (odpoved > cislo):
        print("Tvuj odhad je vetsi")
    elif (odpoved < cislo):
        print("Tvuj odhad je mensi")