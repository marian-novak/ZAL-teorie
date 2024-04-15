try:
    soubor = open("X:/soubor.txt", "w")
    soubor.write("Ahoj ")
    soubor.write("svete\n") 
    soubor.write("Druhy radek\n")
    soubor.close()
except:
    print("Neco se nepovedlo")

try:
    soubor = open("X:/soubo.txt", "r") 
except:
    print("Soubor se nepovedlo otevrit")

try:
    soubor = open("X:/soubor.txt", "r") 
    data = soubor.readline()
    print(data)
    data = soubor.readline()
    print(data)
    data = soubor.readline()
    print(data)
    data = soubor.readline()
    print(data)
except:
    print("Soubor se nepovedlo otevrit")

try:
    soubor = open("X:/soubor.txt", "r")
    for radek in soubor:
        print(radek, end="")
except:
    print("Soubor se nepovedlo otevrit")