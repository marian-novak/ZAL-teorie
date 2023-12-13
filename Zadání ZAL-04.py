rozmer = int(input("Rozmery pole: "))

pole2d = [ [0]*rozmer for i in range(rozmer) ]

if rozmer < 3 or rozmer > 27:
    print("Chyba, moc velke nebo male pole.")

while rozmer >= 3 and rozmer < 27:
    Xzadanex = int(input(""))
    Xzadaney = int(input(""))
    pole2d [Xzadanex][Xzadaney] = "X"
    Ozadanex = int(input(""))
    Ozadaney = int(input(""))
    pole2d [Ozadanex][Ozadaney] = "O"
print(pole2d[2][2])