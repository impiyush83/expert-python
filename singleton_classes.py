class Singleton(type):
    """
    Code for singleton class
    """
    instance = None

    def __call__(cls, *args, **kw):
        if not cls.instance:
            cls.instance = super(Singleton, cls).__call__(*args, **kw)
        return cls.instance


class ASingleton(metaclass=Singleton):
    def __init__(self):
        self.a = 10

    def change(self, num):
        self.a = num

    def __str__(self):
        print(self.a)

    """
    Singleton class
    """
    pass


class RegularClass:
    """
    Regular class
    """
    pass


x = RegularClass()
y = RegularClass()
print(x == y)

# only one instance is created and mulitple objects created point to single instance
a = ASingleton()
b = ASingleton()
print(a == b)

a.change(50)

b.__str__()
a.__str__()
