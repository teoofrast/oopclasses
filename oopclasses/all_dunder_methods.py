class MeansOfTransport():

    def __init__(self, color, brand):
        self.__color = color
        self.__brand = brand

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @color.deleter
    def color(self):
        del self.__color

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand
        
    @brand.deleter
    def brand(self):
        del self.__brand

class Car(MeansOfTransport):

    def __new__(cls, *args, **kwargs):
        print('Вызов метода __new__' + str(cls))
        return super().__new__(cls)

    def __init__(self, color, brand, num_of_wheels):
        print(f'Вызов метода __init__ для {self}')
        super().__init__(color, brand)
        self.__num_of_wheels = num_of_wheels

    @property
    def num_of_wheels(self):
        return self.__num_of_wheels

    @num_of_wheels.setter
    def num_of_wheels(self, num_of_wheels):
        self.__num_of_wheels = num_of_wheels

    @num_of_wheels.deleter
    def num_of_wheels(self):
        del self.__num_of_wheels

    def __getattribute__(self, item):
        print('обращение к атрибуту: ' + item)
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        print('Установка атрибута: ' + key + ' со значением: ' + str(value))
        object.__setattr__(self, key, value)
        # self.__dict__[key] = value

    def __getattr__(self, item):
        print('Обращение к несуществующему свойству: ' + item)

    def __delattr__(self, item):
        print("Удаление " + item)
        object.__delattr__(self, item)

car1 = Car('Black', 'Audi', 4)
del car1.num_of_wheels
print(car1.brand)
print(car1.color)