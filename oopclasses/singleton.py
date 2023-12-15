class Singleton:
    instance = None

    def __new__(cls):
        if Singleton.instance is None:
            Singleton.instance = super().__new__(cls)
        return Singleton.instance

if __name__ == '__main__':
    first = Singleton()
    second = Singleton()
    third = Singleton()
    print(first is second is third)
    