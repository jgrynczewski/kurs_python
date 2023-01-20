class Cow:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other_cow):
        new_name = self.name + other_cow.name
        new_age = self.age + other_cow.age
        c = Cow(new_name, new_age)
        return c

    def __gt__(self, other):
        return self.age > other.age

    def __str__(self):
        return f"Jestem krowa: Cow(name={self.name}, age={self.age})"


c1 = Cow('Mućka', 10)
c2 = Cow('Buffalo', 2)

res = c1 + c2
print(res)

print(c1 > c2)
