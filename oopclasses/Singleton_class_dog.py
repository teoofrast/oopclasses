class Dog:
    __instance = None

    def __new__(cls):
        if Dog.__instance is None:
            Dog__instance = super().__new__(cls)
        return Dog.__instance

if __name__ == '__main__':
    first = Dog()
    second = Dog()
    third = Dog()
    print(first is second is third)
