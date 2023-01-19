# sort method vs sorted function
data = ['a', 'f', 'd', 'b']
# data.sort()

sorted_data = sorted(data)

print(data)
print(sorted_data)

data = [
    [2, 3, 4, 5],
    [4, 5, 3],
    [6, 7]
]


# Sortowanie podlist na podstawie wartości ich ostatniego elementu
def get_last(a_list):
    return a_list[-1]


sorted_data = sorted(data, key=get_last)
print(sorted_data)

# to samo, ale za pomocą funkcji lamdba
sorted_data = sorted(data, key=lambda a_list: a_list[-1])
print(sorted_data)


def square(x):
    return x * x


lambda x: x**2
