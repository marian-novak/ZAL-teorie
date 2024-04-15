pole = {}
def quicksort(pole, low, high):
    pivot = pole[low]
    hranice = low
    for i in range(low+1,high):
        if pole[i] < pivot:
            pole[hranice], pole[i] = pole[i], pole[hranice]
while True:
    input = input("Zadej cislo: ")
    pole.append(int(input))
    if input == "konec":
        break