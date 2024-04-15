import pickle
ucty ={}
uctynovy = {}
while True:
    vsechno = input("Prikaz: ")
    vsechno = vsechno.split(" ")

    if vsechno[0] == "konec":
        break
    try:
        if vsechno[0] == "vklad" and vsechno[1] in ucty:
            if int(vsechno[2]) < 0:
                print("Spatna hodnota cisla")
            else:
                ucty[vsechno[1]].append(int(vsechno[2]))
                print("Vklad", vsechno[2],"na ucet", vsechno[1], "probehl uspesne.")
    except:
        print("Napsal jsi neco spatne lol.")
    try:
        if vsechno[0] == "vklad" and vsechno[1] not in ucty:
            if int(vsechno[2]) < 0:
                print("Spatna hodnota cisla")
            else:    
                ucty[vsechno[1]] = [int(vsechno[2])]
                print("Byl zalozen novy ucet", vsechno[1],".")
                print("Vklad", vsechno[2],"na ucet", vsechno[1], "probehl uspesne.")
    except:
        print("Napsal jsi neco spatne lol.")

    try:
        if vsechno[0] == "vyber" and vsechno[1] in ucty:
            if int(vsechno[2]) < 0:
                print("Spatna hodnota cisla")
            else:
                if sum(ucty[vsechno[1]]) >= int(vsechno[2]): 
                    ucty[vsechno[1]].append(-int(vsechno[2]))
                    print("Vyber", vsechno[2],"z uctu", vsechno[1],"probehl uspesne.")
                else:
                    print("Vyber", vsechno[2], "z uctu", vsechno[1],"selhal: nedostatecny zustatek.")
    except:
        print("Napsal jsi neco spatne lol.")
    try:
        if vsechno[0] == "vyber" and vsechno[1] not in ucty:
            print("Ucet neexsituje.")
    except:
        print("Napsal jsi neco spatne lol.")    
    try:
        if vsechno[0] == "vypis" and vsechno[1] in ucty:
            print("Vypis uctu", vsechno[1])
            for penize in range(len(ucty[vsechno[1]])):
                print(ucty[vsechno[1]][penize])
            print("--------")
            print(sum(ucty[vsechno[1]]), "zustatek")
    except:
        print("Napsal jsi neco spatne lol.")
    try:
        if vsechno[0] == "vypis" and vsechno[1] not in ucty:
            print("Ucet neexistuje")
    except:
        print("Napsal jsi neco spatne lol.")

    try:
        if vsechno[0] == "poplatek":
            if int(vsechno[1]) < 0:
                print("Spatna hodnota cisla")
            else:
                for ucet in ucty:
                    ucty[ucet].append(-int(vsechno[1]))
                print("Zpracovan poplatek", vsechno[1],"na vsech uctech.")
    except:
        print("Napsal jsi neco spatne lol.")

    try:
        if vsechno[0] == "urok":
            if int(vsechno[1]) < 0:
                print("Spatna hodnota cisla")
            else:
                for ucet in ucty:
                    urok = sum(ucty[ucet])*((int(vsechno[1]))/100)
                    ucty[ucet].append(urok)
                print("Zpracovan urok", vsechno[1],"procent na vsech uctech.")
    except:
        print("Napsal jsi neco spatne lol.")

    try:
        if vsechno[0] == "ulozit":
                with open((vsechno[1],".pkl"), "wb") as file:
                    pickle.dump(ucty, file)
                print("Bankovní databáze byla úspěšně uložena.")
    except:
        print("Napsal jsi neco spatne lol.")

    try:
        if vsechno[0] == "nacist":
            with open(vsechno[1], "rb") as file:
                ucty = pickle.load(file)
    except:
        print("Napsal jsi neco spatne lol.")
    if vsechno[0] != "urok" and vsechno[0] != "vklad" and vsechno[0] != "vyber" and vsechno[0] != "poplatek" and vsechno[0] != "vypis" and vsechno[0] != "ulozit" and vsechno[0] != "nacist":
        print("Spatne napsany ci neznamy prikaz. (Zkuste, vklad, urok, poplatek, vypis ci vyber)")