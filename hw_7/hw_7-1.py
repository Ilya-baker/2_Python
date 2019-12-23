class Matrix:
    def __init__(self, sheif):
        self.sheif = sheif

    def __str__(self):
        return '\n'.join(map(str, self.sheif))

    def __add__(self, other):
        list_3 = []
        for i in range(len(self.sheif)):
            list_3.append([])
            for j in range(len(self.sheif[0])):
                list_3[i].append(self.sheif[i][j] + other.sheif[i][j])
        return '\n'.join(map(str, list_3))

list_1 = [[0, 4, 0], [4, 0, 4], [0, 4, 0]]
list_2 = [[1, 3, 1], [3, 1, 3], [1, 3, 1]]

"""Вариант №1"""
print(f"{Matrix(list_1)}\n\n{Matrix(list_2)}\n\n{Matrix(list_1) + Matrix(list_2)}")

"""Вариант №2
matrix_1 = Matrix(list_1)
matrix_2 = Matrix(list_2)
matrix_3 = matrix_1 + matrix_2
print(f"{matrix_1}\n\n{matrix_2}\n\n{matrix_3}")
Мне нравятся оба: первый за локаничность, второй за наглядность. Поэтому высылаю два варианта"""