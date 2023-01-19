# menadżer kontekstu, a co jak plik ma 9999999999 linijek ?
# wczytujemy linijka po linijce

with open('demo.txt', 'r', encoding='utf-8') as f:
    while True:
        content = f.readline()
        if content == "":
            break
        else:
            print(content)
