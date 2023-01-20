# Podnoszenie wyjątków - instrukcja raise

def get_circle_area(r):
    if type(r) == complex:
        raise Exception("Nie obługiwany format - liczby zespolone")
    else:
        return 3.14 * r ** 2


# Kod kliencki
a = get_circle_area(0.1+2j)
a+2

