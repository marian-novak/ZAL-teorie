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

def zjisti_delku_posloupnosti(pole2d, symbol):

    radky = len(pole2d)
    sloupce = len(pole2d[0])

    def zkontroluj_posloupnosti(rad, sloup, delrad, delsloup):
        poc = 0
        while 0 <= rad < radky and 0 <= sloup < sloupce and pole2d[rad][sloup] == symbol:
            poc += 1
            rad += delrad
            sloup += delsloup
        return poc

    def zkontroluj_policko(rad, sloup):
        smery = [(0, 1), (1, 0), (1, 1), (-1, 1)]
        nejdelka = 0
        for delrad, delsloup in smery:
            nejdelka = max(nejdelka, zkontroluj_posloupnosti(rad, sloup, delrad, delsloup) + zkontroluj_posloupnosti(rad, sloup, -delrad, -delsloup) - 1)
        return nejdelka

    nejdelka = 0

    for i in range(radky):
        for j in range(sloupce):
            if pole2d[i][j] == symbol:
                nejdelka = max(nejdelka, zkontroluj_policko(i, j))

    return nejdelka

rozmer = int(input("Rozmery pole: "))

sym_X = "X"
sym_O = "O"

pole2d = [ [0]*rozmer for i in range(rozmer) ]
if rozmer < 3 or rozmer > 27:
    print("Chyba, moc velke nebo male pole.")
pocetkol = 0
while rozmer >= 3 and rozmer < 27:
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
        delka_posloupnosti_X = zjisti_delku_posloupnosti(pole2d, sym_X)
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
        delka_posloupnosti_O = zjisti_delku_posloupnosti(pole2d, sym_O)
        print("Hrac'O': nejdelsi", delka_posloupnosti_O)
    pocetkol += 1