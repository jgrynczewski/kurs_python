# Pliki

# Wczytaj zawartość pliku oda.txt, a następnie zlicz ile znajduje się w
# tekście słów zaczynających się na literę p.

with open('oda.txt', 'r', encoding='utf-8') as f:
    content = f.read()


words_list = content.split()
for word in words_list:
    if word[0] == 'p' or word[0] == "P":
    # if word[0] in ['P', 'p']:
    # if word[0] in 'Pp':
        print(word)
