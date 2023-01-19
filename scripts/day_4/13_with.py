# Zapis do pliku
# w - tryb nadpisywania
# a - tryb dodawania

# trzeba pamiętać o znaku nowej linii

with open('demo.txt', 'a', encoding='utf-8') as f:
    f.write("Ala ma kota\n")
    f.write("Ewa ma psa\n")
