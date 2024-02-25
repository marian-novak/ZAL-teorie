import sys
def kontrola(minuty, hodiny, dny, mesic, rok):
    if minuty > 59 or minuty < 1:
        return False
        print("Chyba!")
    elif minuty < 61 or minuty > 0:
        return True
    if hodiny > 23 or hodiny < 1:
        return False
        print("Chyba!")
    elif hodiny > 0 or hodiny < 25:
        return True
    if mesic > 12 or mesic < 1:
        return False
        print("Chyba!")
    elif mesic > 0 or mesic < 13:
        return True
    if mesic == 1:
        leden = 0
        dny = leden
        if leden > 31 or leden < 1:
            return False
            print("Chyba!")
        else:
            return True
    if mesic == 2 and ((rok % 4 == 0 or rok % 400 == 0) and rok % 4000 != 0 and rok % 100 != 0): 
        punor = 0
        dny = punor
        if punor > 29 or punor < 1:
            return False
            print("Chyba!")
        else:
            return True
    elif mesic == 2:
        unor = 0
        dny = unor
        if unor > 28 or unor < 1:
            return False
            print("Chyba!")
        else:
            return True
    if mesic == 3:
        brezen = 0
        dny = brezen
        if brezen > 31 or brezen < 1:
            return False
            print("Chyba!")
        else:
            return True
    if mesic == 4:
        duben = 0
        dny = duben
        if duben > 30 or duben < 1:
            return False
            print("Chyba!")
        else:
            return True
    if mesic == 5:
        kveten = 0
        dny = kveten
        if kveten > 31 or kveten < 1:
            return False
            print("Chyba!")
        else:
            return True
    if mesic == 6:
        cerven = 0
        cerven = cerven
        if cerven > 30 or cerven < 1:
            return False
            print("Chyba!")
        else:
            return True
    if mesic == 7:
        cervenec = 0
        dny = cervenec
        if cervenec > 31 or cervenec < 1:
            return False
            print("Chyba!")
        else:
            return True
    if mesic == 8:
        srpen = 0
        dny = srpen
        if srpen > 31 or srpen < 1:
            return False
            print("Chyba!")
        else:
            return True
    if mesic == 9:
        zari = 0
        dny = zari
        if zari > 30 or zari < 1:
            return False
            print("Chyba!")
        else:
            return True
    if mesic == 10:
        rijen = 0
        dny = rijen
        if rijen > 31 or rijen < 1:
            return False
            print("Chyba!")
        else:
            return True
    if mesic == 11:
        listopad = 0
        dny = listopad
        if listopad > 30 or listopad < 1:
            return False
            print("Chyba!")
        else:
            return True
    if mesic == 12:
        prosinec = 0
        dny = prosinec
        if prosinec > 31 or prosinec < 1:
            return False
            print("Chyba!")
        else:
            return True
    if rok < 1600:
        return False
        print("Chyba!")
    elif rok > 1599:
        return True
def kontrolaData(cislo):
    try:
        cislo = int(cislo)
        return True
    except ValueError: return False
def kontrolaVstupudatum(indexDatum):
    if len(indexDatum) != 4:
        return False
    else:
        return True
def kontrolaVstupucas(indexCas):
    if len(indexCas) != 2:
        return False
    else:
        return True

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

od = input("Zadejte začátek intervalu ve správném formátu (d. m. r h:min): ")

datumyod = od
datumyod = datumyod.split()
if kontrolaVstupudatum(datumyod) == False:
    print("Chyba!")
    sys.exit()
denodt = datumyod[0]
mesicodt= datumyod[1]
denod = denodt.strip(".")
mesicod = mesicodt.strip(".")
rokod = datumyod[2]
casod = datumyod[3]
casod = casod.split(":")
if kontrolaVstupucas(casod) == False:
    print("Chyba!")
    sys.exit()
minutyod = casod[1]
hodinyod = casod[0]


if kontrolaData(minutyod) == False:
    print("Chyba!")
    sys.exit()
else:
    minutyod = int(minutyod)
if kontrolaData(hodinyod) == False:
    print("Chyba!")
    sys.exit()
else:
    hodinyod = int(hodinyod)
if kontrolaData(denod) == False:
    print("Chyba!")
    sys.exit()
else:
    denod = int(denod)
if kontrolaData(mesicod) == False:
    print("Chyba!")
    sys.exit()
else:
    mesicod = int(mesicod)
if kontrolaData(rokod) == False:
    print("Chyba!")
    sys.exit()
else:
    rokod = int(rokod)
if kontrola(minutyod, hodinyod, denod, mesicod, rokod) == False:
    print("Chyba!")
    sys.exit()

do = input("Zadejte konec intervalu ve správném formátu (d. m. r h:min): ")

datumydo = do
datumydo = datumydo.split()
if kontrolaVstupudatum(datumydo) == False:
    print("Chyba!")
    sys.exit()
dendot = datumydo[0]
mesicdot= datumydo[1]
dendo = dendot.strip(".")
mesicdo = mesicdot.strip(".")
rokdo = datumydo[2]
casdo = datumydo[3]
casdo = casdo.split(":")
if kontrolaVstupucas(casdo) == False:
    print("Chyba!")
    sys.exit()
minutydo = casdo[1]
hodinydo = casdo[0]

if kontrolaData(minutydo) == False:
    print("Chyba!")
    sys.exit()
else:
    minutydo = int(minutydo)
if kontrolaData(hodinydo) == False:
    print("Chyba!")
    sys.exit()
else:
    hodinydo = int(hodinydo)
if kontrolaData(dendo) == False:
    print("Chyba!")
    sys.exit()
else:
    dendo = int(dendo)
if kontrolaData(mesicdo) == False:
    print("Chyba!")
    sys.exit()
else:
    mesicdo = int(mesicdo)
if kontrolaData(rokdo) == False:
    print("Chyba!")
    sys.exit()
else:
    rokdo = int(rokdo)
if kontrola(minutydo, hodinydo, dendo, mesicdo, rokdo) == False:
    print("Chyba!")
    sys.exit()