class MeansOfTransport:

    def __init__(self, color, brand, year_of_manufacture):
        self.color = color
        self.brand = brand
        self.year_of_manufacture = year_of_manufacture

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

    @property
    def year_of_manufacture(self):
        return self.__year_of_manufacture

    @year_of_manufacture.setter
    def year_of_manufacture(self, year_of_manufacture):
        self.__year_of_manufacture = year_of_manufacture

    @year_of_manufacture.deleter
    def year_of_manufacture(self):
        del self.__year_of_manufacture


class Car(MeansOfTransport):

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, color, brand, year_of_manufacture, num_of_wheels, mileage, start_engine=False, counter = 0):
        super().__init__(color, brand, year_of_manufacture)
        self.num_of_wheels = num_of_wheels
        self.__start_engine = start_engine
        self.mileage = mileage
        self.__counter = counter

    @property
    def mileage(self):
        return self.__mileage

    @mileage.setter
    def mileage(self, mileage):
        self.__mileage = mileage

    @mileage.deleter
    def mileage(self):
        del self.__mileage

    @property
    def counter(self):
        return self.__counter

    @property
    def start_engine(self):
        return self.__start_engine

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
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)
        # self.__dict__[key] = value

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        object.__delattr__(self, item)

    def __call__(self, *args, **kwargs):
        if self.__start_engine is False:
            self.__start_engine = "Мотор работает"
            self.__counter += 1
        else:
            self.__start_engine = "Мотор отдыхает"
            self.__counter += 1

    def __repr__(self):
        return f"{str(self.__class__)}"

    def __str__(self):
        return f"Машина бренда: {self.brand} и цветом: {self.color}"

    def __len__(self):
        return 2024 - self.year_of_manufacture

    def __add__(self, other):
        if not isinstance(other, (int, Car)):
            raise ArithmeticError("Не верный тип даных")

        sc = other
        if isinstance(other, Car):
            sc = other.mileage
        return Car(self.color, self.brand, self.year_of_manufacture, self.num_of_wheels, self.mileage + sc)

    # def __eq__(self, other):


car1 = Car("Black", "Mazeratti", 1991, 4, 0)
car1.mileage = 100
car2 = Car("White", "Audi", 1995, 4, 250)
print(f'Машине в 2024 году будет {len(car1)} года/лет')
car3 = car2 + car1
print(car3.mileage)
