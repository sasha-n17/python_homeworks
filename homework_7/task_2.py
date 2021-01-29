from abc import ABC, abstractmethod


class Clothing(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def calc_of_consumption(self):
        pass


class Coat(Clothing):
    @property
    def calc_of_consumption(self):
        return self.param / 6.5 + 0.5


class Suit(Clothing):
    @property
    def calc_of_consumption(self):
        return 2 * self.param + 0.3


coat_test = Coat(13)
print(f'Расход ткани для пальто: {coat_test.calc_of_consumption}')
suit_test = Suit(5)
print(f'Расход ткани для костюма: {suit_test.calc_of_consumption}')
print(f'Суммарный расход ткани: {coat_test.calc_of_consumption + suit_test.calc_of_consumption}')
