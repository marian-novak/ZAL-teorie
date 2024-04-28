import sys
pole2 = ['+A0 : 4', ' -A0 : 1', "lol:1"]
pole1 = ["A1", "A0"]
def rozcisla (pole1, pole2):
    try:
        for i in range(0, len(pole2)):
            je = False
            proc= pole2[i].split(":")
            proc[0] = proc[0].replace(" ","")
            proc[1] = proc[1].replace(" ","")
            if proc[0].strip("+") in pole1:
                proc[0] = proc[0].strip("+")
                for pozice in range(0, len(pole1)):
                    if pole1[pozice] == proc[0]:
                        pozice = pozice
                        je = True
                pole1[pozice] = proc
            if proc[0].strip("-") in pole1:
                proc[0] = proc[0].strip("-")
                for pozice in range(0, len(pole1)):
                    if pole1[pozice] == proc[0]:
                        pozice = pozice
                        je = True
            if je == False:
                return False
    except:
        print("Něco je špatně lol.")
if rozcisla(pole1, pole2) == False:
    sys.exit()
rozcisla(pole1, pole2)
print(pole1)
print(pole2)