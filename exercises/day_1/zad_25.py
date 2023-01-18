# Zad 25 Listy

# Napisz funkcję, która przyjmie listę i wyświetli wszystkie
# elementy tej listy

def iterate_through(param):
    """Implementacja z wykorzystaniem pęlit while"""
    idx = 0
    while idx < len(param):

        elem = param[idx]
        print(elem)

        idx += 1


def iterate_through_2(param):
    """Implementacja z wykorzystaniem pętli for"""

    for elem in param:
        print(elem)


a_list = [-2, 13, 34, 32, 2, 10, 23]
iterate_through_2(a_list)

# docstringi (funkcja help)
help(iterate_through)
