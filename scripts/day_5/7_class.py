# atrybuty obiektowe
# atrybuty klasowe

# metody obiektowe
# metody klasowe
# metody statyczne

class FlyMixin:
    def fly(self):
        print("I can fly")

class Worker:
    def run(self):
        print("Biegnę, biegnę, biegnę")

class Animal:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Hello, world")

class Cow(Animal):
    # Klasa Cow dziedziczy metodę hello rodzica

    group = 'mammals'

    def __init__(self, name, age, sex="F"):
        super().__init__(name)
        self.age = age
        self.sex = sex
        self.homes = []

    def introduce_yourself(self):
        print("Cześć jestem krowa!")

    def say_hello(self):
        print(f"Cześć, nazywam się {self.name}.")

    def change_sex(self):
        if self.sex == 'M':
            self.sex = 'F'
        else:
            self.sex = 'M'

    def add_home(self, name):
        self.homes.append(name)

    @classmethod
    def change_group(cls, name):
        cls.group = name


    @staticmethod
    def evaluate_circle_area(r):
        print(f"Promień koła wynosi {3.14 * r**2}")


class Horse(Animal, Worker):
    # Klasa Horse nadpisuje metodę hello rodzica
    def say_hello(self):
        print("Ihhha, cześć!")

    def hello(self):
        print("Lepsze, Hello, word!")


class Frog(Animal, FlyMixin):
    # klasa Frog rozbudowuje metodę hello rodzica
    def hello(self):
        super().hello()
        print("z moją wstawką")


# Cow.__new__()  # konstruktor - tworzy pusty obiekt
# Cow.__init__()  # inicjalizator - wypełnia pusty obiekt atrybutami


c1 = Cow("Mućka", 2)
c2 = Cow("Buffalo", 1, 'M')

c1.say_hello()
c2.say_hello()

print(c2.sex)
c2.change_sex()
print(c2.sex)

print(c1.homes)
c1.add_home("Zielone Wzgórza")
print(c1.homes)


Cow.change_group('bird')

c1.evaluate_circle_area(10)


c1.hello()  # obiekty klasy Cow dziedziczą metodę hello od Animal

h1 = Horse('Ben')
h1.hello()  # obiekty klasy Horse dziedziczą i nadpisują metodę hello klasy Animal

# Co może zrobić dziecko z metodą rodzica?
# 1. może odziedziczyć
# 2. może nadpisać
# 3. może rozbudować

f1 = Frog('Edward')
f1.fly()
