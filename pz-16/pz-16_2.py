# Создайте базовый класс "Человек" со свойствами "имя", "возраст" и "пол". От этого
# класса унаследуйте классы "Мужчина" и "Женщина" и добавьте в них свойства,
# связанные с социальным положением (например, "семейное положение",
# "количество детей" и т.д.).

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}"

class Man(Person):
    def __init__(self, name, age, marital_status, number_of_children):
        super().__init__(name, age, "Мужчина")
        self.marital_status = marital_status
        self.number_of_children = number_of_children

    def __str__(self):
        return super().__str__() + f", Семейное положение: {self.marital_status}, Количество детей: {self.number_of_children}"

class Woman(Person):
    def __init__(self, name, age, marital_status, number_of_children):
        super().__init__(name, age, "Женщина")
        self.marital_status = marital_status
        self.number_of_children = number_of_children

    def __str__(self):
        return super().__str__() + f", Семейное положение: {self.marital_status}, Количество: {self.number_of_children}"

# Example usage
man1 = Man("John", 30, "Женат", 2)
woman1 = Woman("Jane", 25, "Замужем", 1)

print(man1)
print(woman1)
