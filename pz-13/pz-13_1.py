# Если в матрице имеются положительные элементы, то вывести TRUE, иначе FALSE

def has_positive_elements(matrix):
  for row in matrix:
    for element in row:
      if element > 0:
        return True

  return False


# Пример использования
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[0, 0, 0], [-1, -2, -3], [-4, -5, -6]]

print(has_positive_elements(matrix1))
print(has_positive_elements(matrix2))