def kontrolaDelky(hraciPole, hrac):
        cisx = 0
        cisy = 0
        for diax in range(len(hraciPole[cisx])):
            delka = 0
            retezeni = False
            for diay in range(len(hraciPole[cisy])):
                prvek = hraciPole[cisx][cisy]
                if (prvek == 'X' and retezeni == False): 
                    retezeni = True
                    delka +=1
                    cisy += 1
                    cisx += 1
                    continue
                if (retezeni == True and prvek == 'X'): 
                    delka +=1
                    cisx += 1
                    cisy += 1
                    continue
                else: 
                    if(delka > nejdelsiRetez): nejdelsiRetez = delka
                    retezeni = False
                    delka = 0