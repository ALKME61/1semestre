#32 вариант
#Дан словарь на 6 персон, найти и вывести их средний возраст.

dictWithAges = {
    "Андрей": 32,
    "Кирилл": 29,
    "Даниил": 14,
    "Махмуд": 52
}

print(sum(dictWithAges.values())/len(dictWithAges))