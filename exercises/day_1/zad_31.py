# Zad 31 Listy

# Napisz funkcję, która dla zadanej wartości zwróci listę
# złożoną z liczb parzystych od 0 do tej wartości.

def get_list(num):
    a_list = []
    for item in range(0, num, 2):
        a_list.append(item)

    return a_list


out = get_list(50)
print(out)