# Lambda

# Posortuj elementy słownika po wartościach w tym słowniku
data = {
    "name": "Jan",
    "surname": "Kowalski",
    "city": "Paris",
    "country": "Argentina"
}

tuples_list = data.items()
print(tuples_list)
sorted_tuples_list = sorted(
    tuples_list,
    key=lambda item: item[1],
)
new_dict = dict(sorted_tuples_list)

print(new_dict)
