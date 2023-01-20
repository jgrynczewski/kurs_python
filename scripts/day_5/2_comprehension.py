# Listy składane (list comprehension)
# Stwórz listę od 0 do 10
res = []

for num in range(10):
    res.append(num)

print(res)


r = [num for num in range(10)]
print(r)

# Stwórz listę liczb parzystych od 0 do 10
res = []

for num in range(10):
    if num % 2 == 0:
        res.append(num)

print(res)


r = [num for num in range(10) if num % 2 == 0]
print(r)
