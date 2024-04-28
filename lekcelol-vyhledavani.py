import random
pole = [0] * 777777
for i in range (0,77):
    pole[i] = random.randint(0,1000)

print(pole)
vstup = 1
while(vstup != 0):
    vstup = int(input("Zadej cislo hledane (0 pro konec): "))
    if vstup == "0":
        break
    if vstup in pole:
        print("ANO")
    if vstup not in pole:
        print("NE")