class Bulb:
    def __init__(self, height, turn_on):
        self.__height = height
        self.turn_on = turn_on

    def get_height(self):
        return self.__height

    def set_height(self, new_height):
        self.__height = new_height


c = Bulb(20, True)
height = c.get_height()
print(height)

c.set_height(30)
print(c.get_height())

c.set_height()