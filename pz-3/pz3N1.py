a, b = input('Введите первое число: '), input('Введите второе число: ')
#Ввод чисел


while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели первое число")
        a = input("Введите первое число: ")

while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print("Неправильно ввели второе число")
        b = input("Введите второе число: ")
#Обработчики исключений

if a > 2 and b < 3: print(True)
else: print(False)
