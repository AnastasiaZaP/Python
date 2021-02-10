class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        for row in self.matrix:
            for i in row:
                print(i, end=' ')
            print()
        return ''

# вариант 1:
    def __add__(self, other):
            if len(self.matrix) == len(other.matrix):
                for i in range(len(self.matrix)):
                    for j in range(len(self.matrix[0])):
                        self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
                return Matrix.__str__(self)
            else:
                return '☹ Ничего не получилось - вы пытаетесь сложить разноразмерные матрицы. ' \
                       'Используйте матрицы одинакового размера либо добавьте нули в меньшую матрицу.'

# вариант 2:
    def __add__(self, other):
        new_matrix = []
        if len(self.matrix) == len(other.matrix):
            for i in range(len(self.matrix)):
                new_matrix.append([])
                for j in range(len(self.matrix[0])):
                    if len(self.matrix[i]) == len(other.matrix[i]):
                        new_matrix[i].append(self.matrix[i][j] + other.matrix[i][j])
                    else:
                        return '☹ Ничего не получилось - вы пытаетесь сложить разноразмерные матрицы. ' \
                               'Используйте матрицы одинакового размера либо добавьте нули в меньшую матрицу.'
            return Matrix(new_matrix)
        else:
            return '☹ Ничего не получилось - вы пытаетесь сложить разноразмерные матрицы. ' \
                   'Используйте матрицы одинакового размера либо добавьте нули в меньшую матрицу.'

matrix_1 = Matrix([[1, 2], [3, 4], [11, 12]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])

print("matrix_1:")
print(matrix_1)
print("Сложение matrix_1 и matrix_2 :")
print(matrix_1 + matrix_2)