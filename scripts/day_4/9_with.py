# menadżer kontekstu

with open('demo.txt', 'r', encoding='utf-8') as f:
    content = f.read()  # wczytywanie całej zawartości pliku

# plik zamykany automatycznie po wyjściu z bloku kodu

print(content)
