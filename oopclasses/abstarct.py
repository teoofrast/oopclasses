from abc import ABC, abstractmethod

class Animals(ABC):


    @abstractmethod
    def voice(self):
        pass

    @abstractmethod
    def a(self):
        print('method a')

class Cat(Animals):

    def voice(self):
        print("Meow")


pushok = Cat()
pushok.voice()