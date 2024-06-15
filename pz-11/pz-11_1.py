# Вариант 32.
# 1. Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Элементы первого и второго файлов:
# Количество элементов первого и второго файлов:
# Элементы последней трети:
# Индекс максимального элемента последней трети:

l = [1, 2, 3, 4, 5, 6]
lNega = [-1, -2, -3, -4, -5, -6]

with open('pz-11/1.txt', 'w') as f:
    f.write(", ".join(map(str, l)))

with open('pz-11/2.txt', 'w') as f:
    f.write(", ".join(map(str, lNega)))

with open('pz-11/3.txt', 'w') as f:
    with open("pz-11/1.txt", 'r') as f1:
        f.write(f1.read())
        f.write(', ')
    with open("pz-11/2.txt", 'r') as f2:
        f.write(f2.read())
    f.write('\n' + str(len(lNega) + len(l)))

    # f.write('\n'+', '.join(map(
    #     str,
    #     (l+lNega)[len(l+lNega)//3 * 2:]
    #         )
    #     )
    # )

    biggestOne = max((l+lNega)[len(l+lNega)//3 * 2:])
    f.write("\n" + str(biggestOne))
