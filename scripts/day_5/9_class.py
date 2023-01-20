import abc


class Animal(abc.ABC):
    @abc.abstractmethod
    def fly(self):
        pass


class Horse(Animal):
    def hello(self):
        print("Hello")

    def fly(self):
        print("Latam")


class Frog(Animal):
    def fly(self):
        print("Skaczę, prawie tak że latam")


h = Horse()
f = Frog()


animals = [h, f]
for item in animals:
    item.fly()
