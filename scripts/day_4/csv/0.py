with open('data.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for line in lines:
    attributes = line.split(',')
    print(attributes)