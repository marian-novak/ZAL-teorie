def je_prestupny_rok(rok):
    if ((rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0)) and rok % 4000 != 0:
        return True
    else:
        return False