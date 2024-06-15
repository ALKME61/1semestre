# Создайте класс «Матрица», который имеет атрибуты количества строк и столбцов.
# Добавьте методы для сложения, вычитания и умножения матриц.

import pickle

class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = [[0 for _ in range(columns)] for _ in range(rows)]

    def __str__(self):
        return "\n".join(" ".join(str(x) for x in row) for row in self.matrix)

    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Матрицы должны иметь одинаковые размеры.")
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return result

    def __sub__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Матрицы должны иметь одинаковые размеры.")
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return result

    def __mul__(self, other):
        if self.columns != other.rows:
            raise ValueError(
                "Количество столбцов первой матрицы должно быть равно "
                "количеству строк второй матрицы."
            )
        result = Matrix(self.rows, other.columns)
        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    result.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return result


def save_def(matrix_list):
    with open('pz-16/matrix_data.pkl', 'wb') as f:
        pickle.dump(matrix_list, f)

def load_def():    
    try:
        with open('pz-16/matrix_data.pkl', 'rb') as f:
            matrix_list = pickle.load(f)
        return matrix_list
    except FileNotFoundError:
        return None



# Пример использования
matrix1 = Matrix(2, 3)
matrix1.matrix = [[1, 2, 3], [4, 5, 6]]
matrix2 = Matrix(3, 2)
matrix2.matrix = [[7, 8], [9, 10], [11, 12]]
matrix3 = Matrix(4, 5)
matrix3.matrix = [[4, 5, 6], [7, 8, 9]]

matrix_list = [matrix1, matrix2, matrix3]

save_def(matrix_list)

loaded = load_def()



print("Матрица 1:")
print(matrix1)

print("\nМатрица 2:")
print(matrix2)

# print("\nСложение:")
# print(matrix1 + matrix2)

# print("\nВычитание:")
# print(matrix1 - matrix2)  # Вызовет ValueError, т.к. размеры не совпадают

print("\nУмножение:")
print(matrix1 * matrix2)

print("\nУмножение:")
print(matrix2 * matrix1)

print('\n')

for i in loaded:
    print(i)
