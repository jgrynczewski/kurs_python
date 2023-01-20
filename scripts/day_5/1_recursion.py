# pętli
def count(num):
    res = 0
    for item in range(1, num+1):
        res += item

    return res


r = count(5)
print(r)


# rekurencyjnie
def recursive_count(num):
    # dno rekurencji
    if num == 1:
        return 1

    return num + recursive_count(num-1)


r = recursive_count(5)
print(r)

