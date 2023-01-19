# Wyświetl liczby mniejsze od 50 i podzielne przez 4

# continue - przejdź do kolejnego obrotu pętli ignorując wszystko
# co znajduje się poniżej tej instrukcji (continue)

counter = 0
while counter < 50:
    counter += 1

    if counter % 4 != 0:
        continue

    print(counter)
