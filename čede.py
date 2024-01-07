def zjisti_delku_posloupnosti(pole, symbol):
    # Funkce přijímá 2D pole a symbol (X nebo O) a vrací délku nejdelší posloupnosti symbolů.

    rows = len(pole)
    columns = len(pole[0])

    def zkontroluj_posloupnosti(r, c, dr, dc):
        # Pomocná funkce pro kontrolu posloupností ve směru (dr, dc).
        count = 0
        while 0 <= r < rows and 0 <= c < columns and pole[r][c] == symbol:
            count += 1
            r += dr
            c += dc
        return count

    def zkontroluj_policko(r, c):
        # Kontrola posloupností z aktuálního políčka ve všech směrech.
        directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]  # Všechny směry: vodorovně, svisle, diagonálně.
        max_length = 0
        for dr, dc in directions:
            max_length = max(max_length, zkontroluj_posloupnosti(r, c, dr, dc) + zkontroluj_posloupnosti(r, c, -dr, -dc) - 1)
        return max_length

    max_length = 0

    # Projít všechna políčka a zkontrolovat délku posloupností.
    for i in range(rows):
        for j in range(columns):
            if pole[i][j] == symbol:
                max_length = max(max_length, zkontroluj_policko(i, j))

    return max_length

# Příklad použití:
pole = [
    ['X', 'O', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X', 'O'],
    ['O', 'O', 'X', 'X', 'X'],
    ['X', 'O', 'X', 'O', 'O']
]

symbol_X = 'X'
symbol_O = 'O'

delka_posloupnosti_X = zjisti_delku_posloupnosti(pole, symbol_X)
delka_posloupnosti_O = zjisti_delku_posloupnosti(pole, symbol_O)

print(f"Délka nejdelší posloupnosti X: {delka_posloupnosti_X}")
print(f"Délka nejdelší posloupnosti O: {delka_posloupnosti_O}")