class MeansOfTransport():

    def __init__(self, color, brand):
        self.__color = color
        self.__brand = brand

    def set_color(self, color):
        self.__color = color

    def set_brand(self, brand):
        self.__brand = brand

    def get_color(self):
        return self.__color

    def get_brand(self):
        return self.__brand

class Car(MeansOfTransport):

    def __init__(self, color, brand, num_of_wheels):
        super().__init__(color, brand)
        self.__num_of_wheels = num_of_wheels

class Moped(MeansOfTransport):

    def __init__(self, color, brand, num_of_wheels):
        super().__init__(color, brand)
        self.__num_of_wheels = num_of_wheels

moped1 = Moped('black', 'Kawasaki', 2)
print(moped1.__dict__)
