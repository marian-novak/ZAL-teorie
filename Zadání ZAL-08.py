import sys
pole = [0]*300
for i in range (0,100):
    pole[i] = str("A"+ str(i))
for i in range (100,200):
    pole[i] = str("B"+ str(i-100))
for i in range (200,300):
    pole[i] = str("C"+ str(i-200))

def rozcisla (pole1, pole2):
    for i in pole2:
        pole2[i] = pole2[i].split(":")
        if pole2[i[0]].strip("+") in pole1:
            for pozice in pole1:
                if pole1[pozice] == pole2[i[0]]:
                    return(pozice)
                print("Soubor obsahuje neplatnou událost!")
                sys.exit()
            pole1[pozice].append(int(pole2[i[1]]))
        if pole2[i[0]].strip("-") in pole1:
            for pozice in pole1:
                if pole1[pozice] == pole2[i[0]]:
                    return(pozice)
                print("Soubor obsahuje neplatnou událost!")
                sys.exit()
            pole1[pozice].append(-int(pole2[i[1]]))



codelat = input("Co chceš dělat?: ")
try:
    if codelat == "ulozit":
        covsou = input("Napiš co bude v souboru: ")
        jmenosou1 = input("Napiš jméno souboru: ")
        soubor1 = open(jmenosou1, "w")
        soubor1.write(covsou)
        soubor1.close()
        print("Soubor úspěšně uložen.")
    if codelat == "nacist":
        jmenosou2 = input("Napiš jméno souboru: ")
        soubor2 = open(jmenosou2,"r+")
        covsou = soubor2.read()
        covsou = covsou.split(",")
        print(covsou)
except:
    print("Něco se nepovedlo lol. Zkus to znovu.")