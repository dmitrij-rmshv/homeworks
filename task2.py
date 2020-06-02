# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def fabrics_used(self):
        pass


class Coat(Clothes):

    def __init__(self, size):
        self.v = size

    @property
    def fabrics_used(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, size):
        self.h = size

    @property
    def fabrics_used(self):
        return 2 * self.h + 0.3


my_coat = Coat(56)
my_suit = Suit(189)

print(f'The coat requires {my_coat.fabrics_used:.2f} m of fabric')
print(f'The suit requires {my_suit.fabrics_used:.2f} m of fabric')
