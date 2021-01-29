from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def material_calc(self):
        pass


class Coat(Clothes):
    def __init__(self, size: int):
        self.size = size

    @property
    def material_calc(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, height: int):
        self.height = height

    @property
    def material_calc(self):
        return 2 * self.height + 0.3


suit = Suit(9)
coat = Coat(60)

print(suit.material_calc)
print(coat.material_calc)
