skupiny = [""] * 2

skupiny[0] = "Dne "
skupiny[1] = "Dne "

den1 = input("Jaky je datum prvniho zapasu? ")
den2 = input("Jaky je datum druheho zapasu? ")

skupiny[0] = skupiny[0] + den1 + " hraji: "
skupiny[1] = skupiny[1] + den2 + " hraji: "

vstup = ""
while vstup != "konec":
    vstup = input("Zadej jmeno hrace: ")
    if vstup == "konec":
        break
    skupina = int(input("Zadej cislo skupiny (0,1): "))
    if skupina != 0 and skupina != 1:
        print("Tato skupina neexistuje!")
    else:
        skupiny[skupina] = skupiny[skupina] + vstup + ","

print(skupiny[0])
print(skupiny[1])