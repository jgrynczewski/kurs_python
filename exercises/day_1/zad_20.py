# Zad 20 Funkcje (testy)

# Napisz funkcję, która na wejście przyjmuje jeden symbol,
# a na wyjściu zwraca True, jeżeli podany symbol to samogłoska.
# W przeciwnym razie zwraca False

# is_vowel("y") -> True
# is_vowel("c") -> False

def is_vowel(letter):
    if (
            letter == "a" or
            letter == "e" or
            letter == "i" or
            letter == "o" or
            letter == "u" or
            letter == "y"
    ):
        return True
    else:
        return False


a = "e"

if is_vowel(a):
    print("Cześć, samogłosko!")


# Wersja uproszczona po poznaniu list i operatora członkostwo
# (memebership operator)

def is_vowel2(letter):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    if letter in vowels:
        return True
    else:
        return False


# ciekawostka
def is_vowel3(letter):
    return letter in 'aeiouyAEIOUY'
