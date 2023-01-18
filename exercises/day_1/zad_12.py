# Zad 12 Pętle

# Napisz program, który będzie wyświetlał w pętli kolejne napisy
# wprowadzone przez użytkownika.

# Przykładowe wywołanie:

# >>> Wprwoadź wartość: ala
# Wprowadzono: ala
# Wprowadź wartość: blank
# Wprowadzono wartość: blank
# Wprowadź wartość: exit
# Wprowadzono wartość exit

# hint: Jak wyjść z nieskończonej pęli?
# Sygnał przerwania można wysłać z poziomu terminala przy pomocy
# skrótu klawiszowego ctrl+c


while True:
    res = input("Wprowadź wartość: ")
    print("Wprowadzono wartość: " + res)
