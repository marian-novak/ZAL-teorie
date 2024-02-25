def kontrolaPole (x, y, pole2d):
    if(x > len(pole2d) or y > len(pole2d) or x <= 0 or y <= 0):
        return False
    else:
        return True

def kontrolaStejne (x, y, pole2d):
    if(pole2d[x - 1][y - 1] == 0):
        return True
    else:
        return False

def kontrolaVstupu(cislo):
    try:
        cislo = int(cislo)
        return True
    except ValueError: return False

def zjistidelkuposloupnosti(pole2d, symbol):

    radky = len(pole2d)
    sloupce = len(pole2d[0])

    def zkontrolujposloupnosti(rad, sloup, delrad, delsloup):
        pocet = 0
        while 0 <= rad < radky and 0 <= sloup < sloupce and pole2d[rad][sloup] == symbol:
            pocet += 1
            rad += delrad
            sloup += delsloup
        return pocet

    def zkontrolujpolicko(rad, sloup):
        smery = [(0, 1), (1, 0), (1, 1), (-1, 1)]
        nejdelka = 0
        for delrad, delsloup in smery:
            nejdelka = max(nejdelka, zkontrolujposloupnosti(rad, sloup, delrad, delsloup) + zkontrolujposloupnosti(rad, sloup, -delrad, -delsloup) - 1)
        return nejdelka
    nejdelka = 0
    for i in range(radky):
        for j in range(sloupce):
            if pole2d[i][j] == symbol:
                nejdelka = max(nejdelka, zkontrolujpolicko(i, j))

    return nejdelka
rozmer = int(input("Rozmery pole: "))

sym_X = "X"
sym_O = "O"

pole2d = [ [0]*rozmer for i in range(rozmer) ]
if rozmer < 3 or rozmer > 26:
    print("Chyba, moc velke nebo male pole.")
pocetkol = 0
while rozmer >= 3 and rozmer <= 26:
    if((pocetkol+2) % 2 == 0):
        zadanex = input("")
        if zadanex == "konec":
            break
        if (kontrolaVstupu(zadanex)):
            zadanex = int(zadanex)
        zadaney = input("")
        if zadaney == "konec":
            break
        if (kontrolaVstupu(zadaney)):
            zadaney = int(zadaney)
        if (kontrolaPole(zadanex, zadaney, pole2d) == False):
            print("Tah je mimo pole.")
            break
        if (kontrolaStejne(zadanex, zadaney, pole2d) == False):
            print("Tah uz je v poli.")
            break
        pole2d [zadanex - 1][zadaney - 1] = "X"
        delka_posloupnosti_X = zjistidelkuposloupnosti(pole2d, sym_X)
        print("Hrac'X': nejdelsi", delka_posloupnosti_X)
    else:
        zadanex = input("")
        if zadanex == "konec":
            break
        if (kontrolaVstupu(zadanex)):
            zadanex = int(zadanex)
        zadaney = input("")
        if zadaney == "konec":
            break
        if (kontrolaVstupu(zadaney)):
            zadaney = int(zadaney)
        if (kontrolaPole(zadanex, zadaney, pole2d) == False):
            print("Tah je mimo pole.")
            break
        if (kontrolaStejne(zadanex, zadaney, pole2d) == False):
            print("Tah uz je v poli.")
            break
        pole2d [zadanex - 1][zadaney - 1] = "O"
        delka_posloupnosti_O = zjistidelkuposloupnosti(pole2d, sym_O)
        print("Hrac'O': nejdelsi", delka_posloupnosti_O)
    pocetkol += 1