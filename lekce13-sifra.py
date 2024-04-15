otevrenytext = input("Zadej text k zasifrovani: ")
klic = 0
while (klic == 0):
    try:
        klic = int(input("Zadej cislo jako klic: "))
    except:
        print("To neni platny klic!")