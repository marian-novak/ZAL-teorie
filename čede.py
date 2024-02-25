def kontrola(minuty, hodiny, dny, mesic, rok):
    if minuty > 59 or minuty < 1:
        return False
    if minuty < 61 and minuty > 0:
        return True
    if hodiny > 23 or hodiny < 1:
        return False
    if hodiny < 24 and hodiny > 0:
        return True
    if mesic > 12 or mesic < 1:
        return False
    if mesic < 13 and mesic > 0:
        return True
    if mesic == 1:
        leden = 0
        dny = leden
        if leden > 31 or leden < 1:
            return False
    if mesic == 2 and ((rok % 4 == 0 or rok % 400 == 0) and rok % 4000 != 0 and rok % 100 != 0): 
        punor = 0
        dny = punor
        if punor > 29 or punor < 1:
            return False
    elif mesic == 2:
        unor = 0
        dny = unor
        if unor > 28 or unor < 1:
            return False
    if mesic == 3:
        brezen = 0
        dny = brezen
        if brezen > 31 or brezen < 1:
            return False
    if mesic == 4:
        duben = 0
        dny = duben
        if duben > 30 or duben < 1:
            return False
    if mesic == 5:
        kveten = 0
        dny = kveten
        if kveten > 31 or kveten < 1:
            return False
    if mesic == 6:
        cerven = 0
        cerven = cerven
        if cerven > 30 or cerven < 1:
            return False
    if mesic == 7:
        cervenec = 0
        dny = cervenec
        if cervenec > 31 or cervenec < 1:
            return False
    if mesic == 8:
        srpen = 0
        dny = srpen
        if srpen > 31 or srpen < 1:
            return False
    if mesic == 9:
        zari = 0
        dny = zari
        if zari > 30 or zari < 1:
            return False
    if mesic == 10:
        rijen = 0
        dny = rijen
        if rijen > 31 or rijen < 1:
            return False
    if mesic == 11:
        listopad = 0
        dny = listopad
        if listopad > 30 or listopad < 1:
            return False
    if mesic == 12:
        prosinec = 0
        dny = prosinec
        if prosinec > 31 or prosinec < 1:
            return False
    if rok < 1600:
        return False
    if rok > 1599:
        return True
    else:
        return True