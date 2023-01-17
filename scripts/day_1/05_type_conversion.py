# rzutowanie (zrzutujemy int na str)

# Wbudowane funkcje rzutujące
int()  # rzutuje na int
float()  # rzutuje na float
str()  # rztuje na str
bool()  # rzutuje na boolean
complex()  # rzutuje complex

text = "Wiek Ali: "
age = 45

# rzutujemy age na typ napisowy
stringify_age = str(age)
print(text + stringify_age)

print(str(-4562356643.2414135))

print(int("45"))
print(int("ala ma kota"))  # ta linijka wyrzuca błąd.
# Nie da się zrzutować napisu "ala ma kota" na int.




