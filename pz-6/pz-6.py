# def arithmeticprogression(a1, d):

#   listOfNumbers = []

#   for i in range(10):
#     listOfNumbers.append(a1 + i * d)

#   return listOfNumbers

# a1 = input("Введите a1: ")
# d = input("Введите d: ")

# while type(a1) != int or type(d) != int:
#   try:
#     a1 = int(a1)
#     d = int(d)
#   except ValueError:
#     print("Некорректные данные")
#     a1 = input("Введите a1: ")
#     d = input("Введите d: ")

# print(arithmeticprogression(a1, d))

#######################################################

# def localMin(listOfNumbers):

#   for i in range(1, len(listOfNumbers) - 1):
#     if listOfNumbers[i - 1] > listOfNumbers[i] < listOfNumbers[i + 1]:
#       return listOfNumbers[i]

# listForSearch = input("Введите числа: ").split()

# for i in range(len(listForSearch)):
#   listForSearch[i] = int(listForSearch[i])

# print(listForSearch, ' Первый локальный минимум: ', localMin(listForSearch))

########################################################

def mishmash(listOfNumbers):

  for i in range(0, len(listOfNumbers), 2):
    listOfNumbers[i], listOfNumbers[i+1] = listOfNumbers[i+1], listOfNumbers[i]
  return listOfNumbers

listOfNumbers = input("Введите числа: ").split()
print(mishmash(listOfNumbers))
