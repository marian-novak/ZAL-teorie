text = "Máma mele maso. Ema mele mámu."
print(text)
text = text.swapcase()
print(text)
text = text.capitalize()
print(text)
text = text.split()
print(text)
for slovo in text:
    print(slovo)
cas = "09:11:20"
cas = cas.split(":")
print(cas)
print(cas[0])
print(cas[1])
datum = "10. 3. 2024"
print(datum)
mesic = (datum.split())[1]
print(mesic)
mesic = mesic.strip(".")
print(mesic)
cislosbordelem = ".+-*+*- 1.2    +-+-..*-+..*-"
cislo = cislosbordelem.strip(".+-* ")
print(cislo)

text = "Máma mele maso. Ema mele mámu. Je to maso."
poziceEmy = text.find("Ema")
print(poziceEmy)
print(text[0])
print(text[1])
print(text[2])
print(text[3]) # String(text) = pole znaků !!!
print(len(text)) #text od "Ema" dál je text od poziceEmy do len(text)
textOdEmy = ""
for i in range(poziceEmy, len(text)):
    textOdEmy = textOdEmy + text[i]
print(textOdEmy)