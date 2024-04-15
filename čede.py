ucty = {}

def kontrolaCisla(cislo):
    try:
        cislo = int(cislo)
        return True
    except ValueError: return False

while True:
    vsechno = input("Prikaz: ")
    try:
        vsechno = vsechno.split(" ")
        prikaz = vsechno[0]
        ucetjmeno = vsechno[1]
        ucetpenize = vsechno[2]
    except IndexError:
        try:
            prikaz = vsechno[0]
            urotek = int(vsechno[1])
        except ValueError:
            try:
                prikaz = vsechno[0]
                ucetjmeno = vsechno[1]
            except IndexError:
                prikaz = vsechno[0]
    if kontrolaCisla(ucetpenize) == False:
        print("Špatná hodnota čísla!")
        break
    if prikaz == "konec":
        break
    if prikaz == "vklad" and ucetjmeno not in ucty:
        ucty[ucetjmeno].append(int(ucetpenize))
        print("Byl zalozen novy ucet", ucetjmeno,".")
        print("Vklad", ucetpenize,"na ucet", ucetjmeno, "probehl uspesne.")
    if prikaz == "vklad" and ucetjmeno in ucty:
        ucty[ucetjmeno].append(int(ucetpenize))
        print("Vklad", ucetpenize,"na ucet", ucetjmeno, "probehl uspesne.")
    if prikaz == "vyber" and ucetjmeno in ucty:
        try:
            ucty[ucetjmeno].append(-int(ucetpenize))
            if sum(ucty[ucetjmeno]) < 0:
                raise ValueError
        except ValueError:
            print("Nedostatek penez na ucte.")
    if prikaz == "vyber" and ucetjmeno not in ucty:
        print("Ucet neexsituje.")
    if prikaz == "vypis" and ucetjmeno in ucty:
        print("Vypis uctu", ucetjmeno)
        for penize in range(len(ucty[ucetjmeno])):
            print(ucty[ucetjmeno][penize])
        print("--------")
        print(sum(ucty[ucetjmeno]), "zustatek")
    if prikaz == "poplatek":
        for ucet in ucty:
            ucty[ucet].append(-int(urotek))
    if prikaz == "urok":
        for ucet in ucty:
            urok = sum(ucty[ucet])*(int(urotek))
            ucty[ucet].append(urok)
