class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return other + self.cell

    def __sub__(self, other):
        return other - self.cell

    def __mul__(self, other):
        return other * self.cell

    def __floordiv__(self, other):
        return other // self.cell

    def make_order(self, rows):
        for i in range(int(rows)):
            result = ('❄' * rows + '\n') * (self.cell // rows) + '❄' * (self.cell % rows)
            return result

cell_1 = Cell(67)
cell_2 = Cell(14)
print(f'cell_1 + cell_2 = {cell_1 + cell_2}')
print(f'cell_1 - cell_2 = {cell_1 - cell_2}')
print(f'cell_1 * cell_2 = {cell_1 * cell_2}')
print(f'cell_1 // cell_2 = {cell_1 // cell_2}')
print(f'Разобьем значение cell_2 по рядам:\n{cell_2.make_order(5)}')