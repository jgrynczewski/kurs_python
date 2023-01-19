# Wyświetl liczby mniejsze od 50 i podzielne przez 4
# jeżeli wśród liczb wystąpi 13 przerwij natychmiastowe działanie pętli

# break - natychmiastowe wyjście z pętli

counter = 0
while counter < 50:

    if counter == 13:
        break

    if counter % 4 == 0:
        print(counter)

    counter += 1
