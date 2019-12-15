from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def cons(self):
        pass

class Coat(Clothes):
    @property
    def cons(self):
        return round(self.param / 6.5 + 0.5, 1)

class Costume(Clothes):
    @property
    def cons(self):
        return round(2 * self.param + 0.3, 1)

coat = Coat(51)
costume = Costume(125)
print(f"The coat will take {coat.cons} meters of fabric.")
print(f"The costume will take {costume.cons} meters of fabric.")
