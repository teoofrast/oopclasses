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
    _engine = 2.4
    __transmission = 'auto'

    @classmethod
    def get_class_value(cls):
        return cls._engine, cls.__transmission

    def __init__(self, color, brand, num_of_wheels):
        super().__init__(color, brand)
        self.__num_of_wheels = num_of_wheels

class Moped(MeansOfTransport):

    def __init__(self, color, brand, num_of_wheels):
        super().__init__(color, brand)
        self.__num_of_wheels = num_of_wheels

    @staticmethod
    def find_time(metrs, speed):
        return metrs / speed


moped1 = Moped("Black", "Kawasaki", 2)
car1 =Car('Black', 'Audi', 4)
print(Car._engine)
print(Car.__transmission)
