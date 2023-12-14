class MeansOfTransport:

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

trans1 = MeansOfTransport(input("input a color of vehicle: "), input("input a brand of vehicle: "))
trans1.set_brand(input("Input a new brand of vehicle: "))
print(trans1.__dict__)
