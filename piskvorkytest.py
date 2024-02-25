
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

def zjisti_delku_posloupnosti(pole, symbol):
    rows = len(pole)
    columns = len(pole[0]) if rows > 0 else 0

    def zkontroluj_posloupnost(posloupnost):
        count = 0
        max_count = 0
        for znak in posloupnost:
            if znak == symbol:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        return max_count

    # Zkontrolujte řádky
    nej_delka_radek = max(zkontroluj_posloupnost(pole[i]) for i in range(rows))

    # Zkontrolujte sloupce
    nej_delka_sloupec = max(zkontroluj_posloupnost([pole[i][j] for i in range(rows)]) for j in range(columns))

    # Zkontrolujte hlavní diagonálu
    nej_delka_diagonala_hl = max(zkontroluj_posloupnost([pole[i][i] for i in range(min(rows, columns))]), 0)

    # Zkontrolujte vedlejší diagonálu
    nej_delka_diagonala_ve = max(zkontroluj_posloupnost([pole[i][columns - i - 1] for i in range(min(rows, columns))]), 0)
rozmer = int(input("Rozmery pole: "))

sym_X = "X"
sym_O = "O"

pole2d = [ [0]*rozmer for i in range(rozmer) ]
if rozmer < 3 or rozmer > 27:
    print("Chyba, moc velke nebo male pole.")
pocetkol = 0
while rozmer >= 3 and rozmer <= 27:
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