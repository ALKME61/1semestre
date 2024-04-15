# def sumRowOfNumbers(x, y):
#   row = []
#   for i in range(y - x + 1):
#     row.append(i+x)
#   return sum(row)

# rangeStart = input("Введите начало диапазона: ")
# rangeEnd = input("Введите конец диапазона: ")

# while type(rangeStart) != int or type(rangeEnd) != int:
#   try:
#     rangeStart = int(rangeStart)
#     rangeEnd = int(rangeEnd)
#   except ValueError:
#     print("Вы ввели не целое число!")
#     rangeStart = input("Введите начало диапазона: ")
#     rangeEnd = input("Введите конец диапазона: ")

# print("Сумма численного ряда: ", sumRowOfNumbers(rangeStart, rangeEnd))

#########################################################################

import math

def triangleAreaAndPerimeter(a):
    s = a*a*math.sqrt(3)/4.
    p = a*3
    return p, s

side = input("Введите сторону равностороннего треугольника: ")

while type(side) != int:
    try:
        side = int(side)
    except ValueError:
        print("Вы ввели не целое число!")
        side = input("Введите сторону равностороннего треугольника: ")

print(f'Периметр: {triangleAreaAndPerimeter(side)[0]}, площадь: {round(triangleAreaAndPerimeter(side)[1], 2)}')

