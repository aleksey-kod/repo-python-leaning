from abc import ABC, abstractmethod
class Clothes(ABC):

    def __init__(self, val):
        self.value = val
    @property
    @abstractmethod
    def calculation(self):
        pass
    def __add__(self, other):
        return SumClothes(self.calculation+other.calculation)
    def __str__(self):
        return f'{self.calculation}'

class Coat(Clothes):
    @property
    def calculation(self):
        return round(self.value/6.5)+0.5
class Suit(Clothes):
    @property
    def calculation(self):
        return round((2*self.value + 0.3)/100)

class SumClothes(Clothes):
    @property
    def calculation(self):
        return self.value

coat_1=Coat(40)
suit_1=Suit(180)
print(f'На Пальто 40 размера уйдет {coat_1}')
print(f'На Костюм 180 рост уйдет {suit_1}')
print('На 2 Пальто 40 размера и 2 рост Костюм 180 рост уйдет:')
print(suit_1+coat_1+suit_1+coat_1)
print('На 2 Пальто 40 размера')
print(coat_1+coat_1)
