# Zad 32 Słownik

# Napisz funkcję, która dla zadanego słownika wyświetli powitanie
# zawierające informacje o imieniu użytkownika oraz miejscu jego
# zamieszkania. Przyjmij, że te informacje znajdują się odpowiednio
# pod kluczami name i city tego słownika.

# Przykładowy słownik:


def welcome(person):
    print(f"Witaj, {user['name']} {user['surname']} z miasta {user['city']}")


user = {
    'name': 'Ewa',
    'surname': 'Kowalska',
    'city': 'Wrocław',
    'pesel': 12379413862
}

welcome(user)

person = {
    'name': 'Ewa',
    'surname': 'Kowalska',
    'city': ['Wrocław', 'Łódź'],
    'age': 35
}
