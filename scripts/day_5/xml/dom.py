# 3 different aproach, rather query approach
import xml.dom.minidom

domtree = xml.dom.minidom.parse('people.xml')
group = domtree.documentElement
people = group.getElementsByTagName('person')

for person in people:
    print(f"== Person {person.getAttribute('id')} ==")

    name = person.getElementsByTagName('name')[0].childNodes[0].nodeValue
    age = person.getElementsByTagName('age')[0].childNodes[0].nodeValue
    weight = person.getElementsByTagName('weight')[0].childNodes[0].nodeValue
    height = person.getElementsByTagName('height')[0].childNodes[0].nodeValue

    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Weigth: {weight}")
    print(f"Height: {height}")


# zmieńmy coś
people[0].getElementsByTagName('name')[0].childNodes[0].nodeValue = "Jan Kowalski"
people[0].setAttribute("id", "200")
people[0].setAttribute("newarrt", "Hello")

# możemy również zmieniać nody, dodawać nowe nody lub
# usuwać stare (a nie tylko zmieniać wartości i atrybuty
# ale musimy to robić w stylu dom (myśleć o hierarchi)

new_person = domtree.createElement("person")
new_person.setAttribute("id", "10")

name = domtree.createElement("name")
name.appendChild(domtree.createTextNode("Adam Nowak"))

age = domtree.createElement("age")
age.appendChild(domtree.createTextNode("20"))

weight = domtree.createElement("weight")
weight.appendChild(domtree.createTextNode("80"))

height = domtree.createElement("height")
height.appendChild(domtree.createTextNode("180"))

new_person.appendChild(name)
new_person.appendChild(age)
new_person.appendChild(weight)
new_person.appendChild(height)

group.appendChild(new_person)

# domtree.writexml(open('people.xml', 'w'))

# ładniej
# with open('people.xml', 'w') as f:
#     f.write(domtree.toprettyxml())
