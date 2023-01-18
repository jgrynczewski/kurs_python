# Napisz funkcję, która zwróci listę liczb od 0 do zadaniej liczby
# bez tej liczby.

def get_range(num):
    result = []
    counter = 0
    while counter < num:
        result.append(counter)

        counter += 1

    return result


# for item in get_range(5000):
#     print(item)


for item in range(90, 100, 3):
    print(item)
