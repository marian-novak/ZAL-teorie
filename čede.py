def zjisti_delku_posloupnosti(pole, symbol):

    radky = len(pole)
    sloupce = len(pole[0])

    def zkontroluj_posloupnosti(r, c, dr, dc):
        count = 0
        while 0 <= r < radky and 0 <= c < sloupce and pole[r][c] == symbol:
            count += 1
            r += dr
            c += dc
        return count

    def zkontroluj_policko(r, c):
        directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
        max_length = 0
        for dr, dc in directions:
            max_length = max(max_length, zkontroluj_posloupnosti(r, c, dr, dc) + zkontroluj_posloupnosti(r, c, -dr, -dc) - 1)
        return max_length

    nejdelka = 0

    for i in range(radky):
        for j in range(sloupce):
            if pole[i][j] == symbol:
                nejdelka = max(nejdelka, zkontroluj_policko(i, j))

    return nejdelka

# Příklad použití:
pole = [
    ['X', 'O', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X', 'O'],
    ['O', 'O', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'O', 'O']
]

symbol_X = 'X'
symbol_O = 'O'

delka_posloupnosti_X = zjisti_delku_posloupnosti(pole, symbol_X)
delka_posloupnosti_O = zjisti_delku_posloupnosti(pole, symbol_O)

print(f"Délka nejdelší posloupnosti X: {delka_posloupnosti_X}")
print(f"Délka nejdelší posloupnosti O: {delka_posloupnosti_O}")