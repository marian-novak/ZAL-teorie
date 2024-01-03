rozmer = int(input("Rozmery pole: "))

pole2d = [ [0]*rozmer for i in range(rozmer) ]

if rozmer < 3 or rozmer > 27:
    print("Chyba, moc velke nebo male pole.")

while rozmer >= 3 and rozmer < 27:
    Xzadanex = int(input("")) - 1
    Xzadaney = int(input("")) - 1
    pole2d [Xzadanex][Xzadaney] = "X"
    print(Xzadanex, Xzadaney)
    Ozadanex = int(input("")) - 1
    Ozadaney = int(input("")) - 1 
    pole2d [Ozadanex][Ozadaney] = "O"
    print(Ozadanex, Ozadaney)
print(pole2d[2][2])

