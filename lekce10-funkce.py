import math

def vzdalenost(x1, y1, x2, y2):
    x = x1 - x2
    y = y1 - y2
    vzdalenost = math.sqrt(x*x + y*y)
    return vzdalenost

def nejdelsiposloupnost(pole):
    i = 0
    velikost = (len(pole))
    predchozi = pole[0]
    delka = 1
    while i < velikost:
        if pole[i] == predchozi:
            delka += 1
        else:
            print("Posloupnost ", predchozi, "je dlouha ", delka)
            predchozi = pole[i]
            delka = 1
        i = i + 1

mojepole = [0]*20
mojepole[2] = 1
mojepole[3] = 1
mojepole[10] = 1
mojepole[11] = 1
mojepole[12] = 1
mojepole[18] = 1
nejdelsiposloupnost(mojepole)