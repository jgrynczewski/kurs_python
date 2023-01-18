# Zad 26 Listy

# Napisz funkcję, która przyjmuje listę i zwraca sumę elementów
# tej listy.

def get_sum(a_list):
    a_sum = 0
    idx = 0
    while idx < len(a_list):

        elem = a_list[idx]
        a_sum += elem

        idx += 1

    return a_sum


data = [1, 4, 6, 7, 8]


result = get_sum(data)
print(result)
