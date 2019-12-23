class Cells:
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return self.param

    def __add__(self, cell_add):
        return f'Sum of cells = {self.param + cell_add.param}'

    def __sub__(self, cell_sub):
        return self.param - cell_sub.param if self.param - cell_sub.param > 0 \
            else "The difference is greater than or equal to zero."

    def __mul__(self, cell_mul):
        return f'Multiply of cells = {self.param * cell_mul.param}'

    def __truediv__(self, cell_dev):
        return f'Division of cells = {round(self.param / cell_dev.param)}'

    def make_order(self, rows):
        return '\n'.join(['o' * rows for _ in range(self.param // rows)]) + '\n' + 'o' * (self.param % rows)

cell_1 = Cells(18)
cell_2 = Cells(39)

print('\n'.join([cell_1 + cell_2, cell_1 - cell_2, cell_1 * cell_2, cell_1 / cell_2, cell_2.make_order(5)]))


