a = [3, 4, 2, 3, 4, 5, 6, 6, 7, 8, 7]

b = []
for item in a:
    if item not in b:
        b.append(item)

print(b)

# Zbiory nie mogą mieć powtórzeń (usuwają powtórzenia)

print(a)
print(set(a))
print(list(set(a)))

# macierz
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# numpy
# scipy
