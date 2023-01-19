# Opcjonalne parametry funkcji open

# Rodzaje plików:
# b - binarny
# t - teksty

# Cztery tryby otwarcia pliku:
# r - otwarcie pliku w trybie do odczytu
# w - otwarcie pliku w trybie do nadpisywania
# a - otwarcie pliku w trybie do dodawania
# x - stworzenie pliku

f = open('demo.txt', 'r', encoding='utf-8')  # otwarcie pliku w trybie do odczytu
# i kodowaniem utf-8

content = f.read()

f.close()  # zamknięcie pliku

print(content)
