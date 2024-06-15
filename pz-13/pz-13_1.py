# Если в матрице имеются положительные элементы, то вывести TRUE, иначе FALSE

def process_matrix(matrix):
  evenElements = [
      element for row in matrix for element in row
      if element > 0 and element % 2 == 0
  ]

  sumElements = sum(evenElements)
  average = sumElements / len(evenElements) if evenElements else 0

  return evenElements, sumElements, average


# Пример использования
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
]

for i in matrix:
  print(i)

evenElements, sumElements, average = process_matrix(matrix)

print("Положительные четные элементы:", evenElements)
print("Сумма:", sumElements)
print("Среднее арифметическое:", average)
