from abc import ABC, abstractmethod
class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def my_method(self):
        pass

    @property
    def sum(self):
        return f'Сумма затраченной ткани {(self.param/6.5 + 0.5) + (2 * self.param + 0.3):.2f}'

class Coat(Clothes):
    def my_method(self):
        pass

    def sum(self):
        return f'Для пошива пальто нужно {(self.param / 6.5 + 0.5):.2f} ткани'

class Сostume(Clothes):
    def my_method(self):
        pass

    def sum(self):
        return f'Для пошива костюма нужно {(2 * self.param + 0.3):.2f} ткани'

coat = Coat(500)
costume = Сostume(600)
print(coat.sum())
print(costume.sum())
