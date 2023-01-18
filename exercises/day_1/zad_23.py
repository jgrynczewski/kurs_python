# Zad 23 Funkcje (pętla i print)

# Napisz funkcję, która dla zadanej liczby wyświetli wszystkie
# liczby parzyste od zera do tej liczby (bez tej liczby).


def print_even(lim):

    counter = 0
    while counter < lim:
        counter += 1

        if counter % 2 == 0:
            print(counter)


print_even(50)
