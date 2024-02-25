casod = "A"
casdo = "A"
denod = "A"
minutyod = "A"
rokod = "A"
mesicod = "A"
hodinyod = "A"
dendo = "A"
minutydo = "A"
rokdo = "A"
mesicdo = "A"
hodinydo = "A"
kkt = 1
while kkt == 1:
    od = input("Zadejte začátek intervalu: ")
    do = input("Zadejte konec intervalu: ")

    datumyod = od
    denod = (datumyod.split())[0]
    mesicod = (datumyod.split())[1]
    rokod = (datumyod.split())[2]
    casod = (datumyod.split())[3]
    minutyod = (casod.split(":"))[1]
    hodinyod = (casod.split(":"))[0]

    print(minutyod)
    print(hodinyod)
    print(rokod)
    print(mesicod)
    print(denod)
    break

def spatnezadany (listdatum, listcas)
    if len(listdatum) != 4:
        print("Špatně zadaný formát, musíš dát: d. měs. r h:min ")

def kontrola(minuty, hodiny, dny, mesic, rok):
    if minuty > 59 or minuty < 1:
        return False
            print("Chyba!")
            break
    elif minuty < 59 or minuty > 1:
        return True
    if hodiny > 23 or hodiny < 1:
        return False
        print("Chyba!")
        break
        else:
            return True
    if mesic > 12 or mesic < 1:
        return False
        print("Chyba!")
        break
        else:
            return True
    if mesic == 1:
        leden = 0
        dny = leden
        if leden > 31 or leden < 1:
            return False
            print("Chyba!")
            break
            else:
                return True
    if mesic == 2 and ((rok % 4 == 0 or rok % 400 == 0) and rok % 4000 =! 0 and rok % 100 =! 0): 
        punor = 0
        dny = punor
        if punor > 29 or punor < 1:
            return False
            print("Chyba!")
            break
        else:
            return True
    elif mesic == 2:
        unor = 0
        dny = unor
        if unor > 28 or unor < 1:
            return False
            print("Chyba!")
            break
        else:
            return True
    if mesic == 3:
        brezen = 0
        dny = brezen
        if brezen > 31 or brezen < 1:
            return False
            print("Chyba!")
            break
        else:
            return True
    if mesic == 4:
        duben = 0
        dny = duben
        if duben > 30 or duben < 1:
            return False
            print("Chyba!")
            break
        else:
            return True
    if mesic == 5:
        kveten = 0
        dny = kveten
        if kveten > 31 or kveten < 1:
            return False
            print("Chyba!")
            break
        else:
            return True
    if mesic == 6:
        cerven = 0
        cerven = cerven
        if cerven > 30 or cerven < 1:
            return False
            print("Chyba!")
            break
        else:
            return True
    if mesic == 7:
        cervenec = 0
        dny = cervenec
        if cervenec > 31 or cervenec < 1:
            return False
            print("Chyba!")
            break
        else:
            return True
    if mesic == 8:
        srpen = 0
        dny = srpen
        if srpen > 31 or srpen < 1:
            return False
            print("Chyba!")
            break
        else:
            return True
    if mesic == 9:
        zari = 0
        dny = zari
        if zari > 30 or zari < 1:
            return False
            print("Chyba!")
            break
        else:
            return True
    if mesic == 10:
        rijen = 0
        dny = rijen
        if rijen > 31 or rijen < 1:
            return False
            print("Chyba!")
            break
        else:
            return True
    if mesic == 11:
        listopad = 0
        dny = listopad
        if listopad > 30 or listopad < 1:
            return False
            print("Chyba!")
            break
        else:
            return True
    if mesic == 12:
        prosinec = 0
        dny = prosinec
        if prosinec > 31 or prosinec < 1:
            return False
            print("Chyba!")
            break
        else:
            return True
    if rok < 1600:
        return False
        print("Chyba!")
        break
    else:
        return True