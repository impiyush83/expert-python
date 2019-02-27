# Abstract classes cannot be instantiated, but they can be subclassed

import abc


class MyABC1(metaclass=abc.ABCMeta):
    pass


# OR


class MyABC2(abc.ABC):
    pass


# SNIPPET

class MyABC3(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def mandatory_inplementation(self): # abstract mandatory implementation
        pass


class InheritsAbstractClass(MyABC3):
    def mandatory_inplementation(self):
        return "This is mandatory implementation in child class"
    pass


obj = InheritsAbstractClass()
print(obj.mandatory_inplementation())
