# Obsługa wyjątków - klauzula try/except

# LBYL - Look Before You Leap
# num = input("Podaj dzielnik: ")
# if num.isdecimal():
#     num = float(num)
#     if num == 0:
#         print("Nie można dzielić przez 0")
#     else:
#         ans = 100 / num
#         print(ans)
# else:
#     print("Podano nieprawidłową wartość")


# EAFP - Easier Ask Forgiveness than Permission
num = input("Podaj dzielnik: ")
try:
    div = int(num)
    ans = 100 / div
except ZeroDivisionError:
    print("Nie można dzielić przez 0!")
except ValueError:
    print("Podano nieprawidłową wartość")
else:  # jeżelie nie było wyjątku
    print(ans)
finally:  # zawsze
    print("Koniec.")
