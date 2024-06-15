# В последовательности на n целых чисел умножить все элементы на первый
# максимальный элемент

li = [4, 5, 3, 4, 5, 6, 7]

maximum = lambda n: max(n)

prod = lambda n: ''.join(str([i * maximum(n[:2]) for i in n]))
print(prod(li))