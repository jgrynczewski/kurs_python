x = int(input("Podaj swój wiek: "))

if x < 16:
    print("Wejście niedozwolone")
elif x < 18:
    print("Możesz wejść z opiekunem")
elif x < 21:
    print("Możesz wejść bez opiekuna")
else:
    print("Możesz wszystko")
