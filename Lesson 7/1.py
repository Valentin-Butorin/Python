class Matrix:
    def __init__(self, matrix: list):
        self.matrix = matrix

    def __str__(self):
        return str(self.matrix)

    def __add__(self, other):
        def gen(s):
            for el in s:
                yield el

        a_gen = gen(self.matrix)
        b_gen = gen(other.matrix)
        result = [list(map(sum, zip(next(a_gen), next(b_gen)))) for _ in range(len(self.matrix))]
        return Matrix(result)


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [2, 3, 4], [7, 8, -2]])
matrix_2 = Matrix([[2, 3, 4], [5, 6, 7], [3, 4, 5], [6, -1, -8]])
matrix_3 = Matrix([[3, 4, 5], [6, 7, 8], [4, 5, 6], [-3, -4, -7]])
matrix_4 = matrix_1 + matrix_2 + matrix_3
print(matrix_1)
print(matrix_2)
print(matrix_3)
print(matrix_4)
