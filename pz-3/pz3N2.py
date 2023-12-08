colors = {
    '0-450': 'Фиолетовый',
    '450-480': 'Синий',
    '480-510': 'Сине-зелёный',
    '510-550': 'Зелёный',
    '550-570': 'Жёлто-зелёный',
    '570-590': 'Жёлтый',
    '590-630': 'Оранжевый',
    '630-1000': 'Красный'
}
# Создали словарь с цветами, ключами к которым является их диапазон, позже используем их в качестве условия, чтобы не создать большую конструкцию if elif 

keysOfColorsList = list(colors.keys())
# Добавили ключи в список, для более удобной работы с ними

a = input("Введите длину волны: ")
#Просим пользователя ввести длину волны

while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите длину волны: ")


for i in range(len(keysOfColorsList)):
    min = keysOfColorsList[i].split('-')[0]
    max = keysOfColorsList[i].split('-')[1]
    if a >= int(min) and a < int(max): print(colors[keysOfColorsList[i]])
    else: continue

#Проходимся циклом по диапазонам, сравнивая их с введённой длиной волны пользователем
#min и max появились в результате разделения через сплит, левое значение min, правое соответственно max
#Если мы нашли нужный диапазон, то используя элемент массива, который является ключем к цвету выводим название этого цвета