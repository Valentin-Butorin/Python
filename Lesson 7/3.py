class Cell:
    def __init__(self, cell: int):
        self.cell = cell

    def __str__(self):
        return str(self.cell)

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        if self.cell <= other.cell:
            return 'Отрицательный результат.'
        return Cell(self.cell - other.cell)

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __floordiv__(self, other):
        return Cell(self.cell // other.cell)

    def make_order(self, raw: int):
        result_list = []
        for i in range(1, self.cell + 1):
            if i % raw == 0:
                result_list.append('*' * raw)
            elif i == self.cell:
                result_list.append('*' * (self.cell - len(result_list) * raw))
        return '\n'.join(result_list)


cell_1 = Cell(12)
cell_2 = Cell(5)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_2 - cell_1)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_1.make_order(5))
