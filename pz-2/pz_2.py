L = input('Введите расстояние в см: ')

while type(L) != int:
    try:
        print("Результат в метрах: " + str(int(L) / 100))
        break
    except ValueError:
        print("Вы ввели не число")
        L = input('Введите расстояние в см: ')