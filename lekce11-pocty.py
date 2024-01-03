#pole = [1,1,2,3,4,1,1,5,3,4,2,1,1,2,2,2,4,3,1]
#print(pole)
#def nejvetcislo(pole):
#    if len(pole)>0:
#        max = pole[0]
#    else:
#        return 0    
#    for x in pole:
#        if x > max:
#            max = x
#    return max
#def nejcastcislo(pole):
#    max = nejvetcislo(pole)
#    cetnost = [0] * (max+1)
#    for x in pole:
#        cetnost[x] = cetnost[x] + 1
#    return nejvetcislo(cetnost)[1]

pole = [1, 2, 2, 3, 4, 1, 1, 5, 3, 4, 2, 1, 6, 2, 2, 2, 7, 3, 2, 1, 2, 3 ,4, 1, 2, 1]
print(pole)

def nejvetsiCislo(pole):
    if len(pole)>0: # kontrola, zda pole neni prazdne
        maximum = pole[0] # dosavadni maximum je prvni prvek
        maxIndex = 0
    else:
        return 0 # pri prazdnem poli vrati nulu
    ## pomoci for
    #for x in pole: # pro kazdy prvek z pole proved:
    #    if x > maximum: # pokud je prvek v poli vetsi, nez maximum
    #        maximum = x # uloz nove maximum

    ## pomoci while
    index = 0
    while index < len(pole):
        if pole[index] > maximum:
            maximum = pole[index]
            maxIndex = index
        index = index + 1

    return [maximum, maxIndex]

# Funkce, ktera najde nejcastejsi cislo
# Vim, ze nejmensi cislo je 1
def nejcastejsiCislo(pole):
    maximum = nejvetsiCislo(pole)[0]
    cetnost = [0] * (maximum+1)
    for x in pole:
        cetnost[x] = cetnost[x] + 1
    return nejvetsiCislo(cetnost)[1]

print(nejcastejsiCislo(pole))

