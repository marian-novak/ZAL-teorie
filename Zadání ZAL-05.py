import sys
def kontrolaMinuty(minuty):
    if minuty > 60 or minuty < 0:
        return False
    else:
        return True
def kontrolaHodiny(hodiny):
    if hodiny > 23 or hodiny < 0:
        return False
    else:
        return True
def kontrolaRok(rok):
    if rok < 1600:
        return False
    else:
        return True
def kontrolaMesic(mesic):
    if mesic > 12 or mesic < 1:
        return False
    else:
        return True
def kontrolaDen(den, mesic, rok):
    if mesic == 1 and (den < 1 or den > 31):
        return False
    if mesic == 2 and rok % 4 == 0 and (rok % 400 + rok % 100 == 0) and (den < 1 or den > 29) and rok % 4000 != 0:
        return False
    if mesic == 2 and (den < 1 or den > 28) and (rok % 4 != 0 or (rok % 400 + rok % 100 != 0) or rok % 4000 == 0):
        return False
    if mesic == 3 and (den < 1 or den > 31):
        return False
    if mesic == 4 and (den < 1 or den > 30):
        return False
    if mesic == 5 and (den < 1 or den > 31):
        return False
    if mesic == 6 and (den < 1 or den > 30):
        return False
    if mesic == 7 and (den < 1 or den > 31):
        return False
    if mesic == 8 and (den < 1 or den > 31):
        return False
    if mesic == 9 and (den < 1 or den > 30):
        return False    
    if mesic == 10 and (den < 1 or den > 31):
        return False
    if mesic == 11 and (den < 1 or den > 30):
        return False
    if mesic == 12 and (den < 1 or den > 31):
        return False
    else:
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
def kontrolaJestliJeOdVetsiNeJesteDelsiTatoDefiniceNemuzeBytLolololololo(minutyod, hodinyod, dnyod, mesicod, rokod, minutydo, hodinydo, dendo, mesicdo, rokdo):
    if rokod > rokdo:
        return False
    if mesicod > mesicdo and rokod >= rokdo:
        return False
    if denod > dendo and mesicod >= mesicdo and rokod >= rokdo:
        return False
    if hodinyod > hodinydo and denod >= dendo and mesicod >= mesicdo and rokod >= rokdo:
        return False
    if minutyod >= minutydo and hodinyod >= hodinydo and denod >= dendo and mesicod >= mesicdo and rokod >= rokdo:
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
kuku = 0

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
if kontrolaMinuty(minutyod) == False:
    print("Chyba!")
    sys.exit()
if kontrolaHodiny(hodinyod) == False:
    print("Chyba!")
    sys.exit()
if kontrolaRok(rokod) == False:
    print("Chyba!")
    sys.exit()
if kontrolaMesic(mesicod) == False:
    print("Chyba!")
    sys.exit()
if kontrolaDen(denod, mesicod, rokod) == False:
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
if kontrolaMinuty(minutydo) == False:
    print("Chyba!")
    sys.exit()
if kontrolaHodiny(hodinydo) == False:
    print("Chyba!")
    sys.exit()
if kontrolaRok(rokdo) == False:
    print("Chyba!")
    sys.exit()
if kontrolaMesic(mesicdo) == False:
    print("Chyba!")
    sys.exit()
if kontrolaDen(dendo, mesicdo, rokdo) == False:
    print("Chyba!")
    sys.exit()
if kontrolaJestliJeOdVetsiNeJesteDelsiTatoDefiniceNemuzeBytLolololololo(minutyod, hodinyod, denod, mesicod, rokod, minutydo, hodinydo, dendo, mesicdo, rokdo) == False:
    print("Chyba!")
    sys.exit()

while minutyod != minutydo:
    if mesicod == 1 and denod == 31:
        mesicod += 1
        denod = 1
    if mesicod == 2 and denod and (rokod % 4 != 0 or (rokod % 400 + rokod % 100 != 0) or rokod % 4000 == 0):
        mesicod += 1
        denod = 1
    if mesicod == 2 and rokod % 4 == 0 and (rokod % 400 + rokod % 100 == 0) and rokod % 4000 != 0 and denod == 29:
        mesicod += 1
        denod = 1
    if mesicod == 3 and denod == 31:
        mesicod += 1
        denod = 1
    if mesicod == 4 and denod == 30:
        mesicod += 1
        denod = 1
    if mesicod == 5 and denod == 31:
        mesicod += 1
        denod = 1
    if mesicod == 6 and denod == 30:
        mesicod += 1
        denod = 1
    if mesicod == 7 and denod == 31:
        mesicod += 1
        denod = 1
    if mesicod == 8 and denod == 31:
        mesicod += 1
        denod = 1
    if mesicod == 9 and denod == 30:
        mesicod += 1
        denod = 1
    if mesicod == 10 and denod == 31:
        mesicod += 1
        denod = 1
    if mesicod == 11 and denod == 30:
        mesicod += 1
        denod = 1
    if mesicod == 12 and denod == 31:
        mesicod = 1
        denod = 1
        rokod += 1
    if hodinyod == 24:
        hodinyod = 0
        denod += 1
    if minutyod < 60:
        minutyod += 1
    if minutyod == 30:
        kuku += 1
    if minutyod == 60 and hodinyod > 12 and hodinyod != 0:
        kuku += (hodinyod - 12)
        minutyod = 0
        hodinyod += 1
    if minutyod == 60 and hodinyod < 13 and hodinyod != 0:
        kuku += hodinyod
        minutyod = 0
        hodinyod += 1
    if minutyod == 60 and hodinyod == 0:
        kuku += 12
        minutyod = 0
        hodinyod += 1

print("Kukačka zakukala", kuku,"x")