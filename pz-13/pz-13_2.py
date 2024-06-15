# В матрице найти сумму и произведение элементов строки N (N задать с клавиатуры).

def sum_and_product_of_column(matrix, colIndex):
  
  colSum = 0
  colProduct = 14

  for row in matrix:
    if colIndex < len(row):
      colSum += row[colIndex]
      colProduct *= row[colIndex]

  return colSum, colProduct

matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
]

colIndex = int(input("Индекс столбца: "))

colSum, colProduct = sum_and_product_of_column(matrix, colIndex)

print(f"Сумма элементов столбца {colIndex}: {colSum}")
print(f"Произведение элементов столбца {colIndex}: {colProduct}")