print(range(10))

# zwykła funkcja
def my_range(num):
    idx = 0
    result = []
    while idx < num:
        result.append(idx)
        idx += 1

    return result


# res = my_range(999999)
# print(res)


# generator
def my_range2(num):
    idx = 0
    result = []
    while idx < num:
        yield idx
        idx += 1

# zwykła funkcja
# for item in my_range(999999999999999999999999999):
#     print(item)


# generator
# for item in my_range2(999999999999999999999999):
#     print(item)

