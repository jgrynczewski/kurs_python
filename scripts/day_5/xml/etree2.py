import xml.etree.ElementTree as ET

tree = ET.parse('people2.xml')
root = tree.getroot()
print(ET.tostring(root))  # -> bit string

# Podgląd atrybutu
launched = root.get('launched')
print(launched)

# Ustawienie atrybutu
root.set('launched', '2023-01-20')
print(root.attrib)

# save
tree.write('people2.xml')

# Dodawanie atrybutu do wszystkich person
# findAll
# ElementTree

number = 100
for person in tree.findall('person'):
    person.set('number', str(number))
    number += 20

tree.write('people2.xml')

# Usuwanie atrybutu
for person in tree.findall('person'):
    del(person.attrib['number'])

# Dodawanie nodów
# metoda 1
person1 = ET.fromstring("<person>Ala Kowalska</person>")
root.append(person1) # formatting
tree.write('people2.xml')

# metoda 2
person2 = ET.Element("person")
person2.text = 'John Doe'
root.append(person2)
tree.write('people2.xml')


# Wybieranie elementów po ścieżce