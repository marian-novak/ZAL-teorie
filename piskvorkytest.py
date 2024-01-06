import math

def nejdelsiposloupnost(pole):
    i = 0
    i2 = 0
    i3 = 0
    velikostx = (len(pole))
    velikosty = (len(pole))
    predchozi = pole[0][0]
    delka = 1
    while i < velikostx or velikosty:
        if pole[i] or pole[i2] or pole[i3] == predchozi:
            delka += 1
        else:
            print("Posloupnost ", predchozi, "je dlouha ", delka)
            predchozi = pole[i]
            delka = 1
        i = i + 1

mojepole = [ ["O"]*20 for i in range(20) ]
mojepole[5][1] = "X"
mojepole[6][3] = "X"
mojepole[9][8] = "O"
mojepole[1][2] = "X"
mojepole[4][3] = "O"
mojepole[19][2] = "O"
mojepole[2][19] = "O"
mojepole[3][19] = "X"
mojepole[10][11] = "X"
mojepole[11][11] = "X"
mojepole[12][4] = "X"
mojepole[18][12] = "X"
nejdelsiposloupnost(mojepole)