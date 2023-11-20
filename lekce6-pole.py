pocet = int(input("Kolik chces zadat cisel?: "))
polecisel = [69] * pocet

i = 0
while i < pocet:
    polecisel[i] = int(input("Cislo: "))
    i = i + 1

i = 0

while i < pocet:
    print(polecisel[i])
    i = i + 1