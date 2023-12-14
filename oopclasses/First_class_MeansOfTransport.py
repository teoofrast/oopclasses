class MeansOfTransport:

    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def show_color(self):
        return self.color

    def show_brand(self):
        return self.brand


trans1 = MeansOfTransport(input(), input())
print(trans1.show_brand(), trans1.show_color())
