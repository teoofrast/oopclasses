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

trans1 = MeansOfTransport(input("Введите цвет транспорта: "), input("Введите марку транспорта: "))
trans1.set_brand(input("Введите новую марку транспорта: "))
print(trans1.__dict__)
