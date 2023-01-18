# Zad 13 Pętle

# Napisz program, który będzie wyświetlał w pętli kolejne napisy wprowadzone przez użytkownika.
# Jeżeli użytkownik wprowadzi wartość 'blank' będzie ona ignorowana. Przykładowe wywołanie:

# >>> Wprwoadź wartość: ala
# Wprowadzono: ala
# Wprowadź wartoć: blank
# Wprowadź wartość: exit
# Wprowadzono wartość exit

# hint: Jak wyjść z nieskończonej pęli?
# Sygnał przerwania można wysłać z poziomu terminala przy pomocy skrótu klawiszowego ctrl+c

while True:
    res = input("Wprowadź wartość: ")

    if res == 'blank':
        continue

    print("Wprowadzono wartość: " + res)
