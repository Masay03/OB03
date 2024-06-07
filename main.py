# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы
# (`make_sound()`, `eat()`) для всех животных.
#
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
#
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и
# вызывает метод `make_sound()` для каждого животного.
#
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
#
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы
# (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

import pickle

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} издает звук.")

    def eat(self):
        print(f"{self.name} ест.")

class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} издает громчёнок.")

class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} издает молот.")

class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} издает звук.")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

bird = Bird("Попугай", 2)
mammal = Mammal("Кошка", 5)
reptile = Reptile("Леопард", 3)

animals = [bird, mammal, reptile]
animal_sound(animals)

class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Добавлен {animal.name} в зоопарк.")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Добавлен {employee.name} в штат зоопарка.")
class Employee:
    def __init__(self, name):
        self.name = name

class ZooKeeper(Employee):
    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")

class Veterinarian(Employee):
    def heal_animal(self, animal):
        print(f"{self.name} исцеляет {animal.name}.")

def save_zoo(zoo, filename):
    with open(filename, 'wb') as file:
        pickle.dump(zoo, file)
    print(f"Данные зоопарка, сохраненные в {filename}")

def load_zoo(filename):
    try:
        with open(filename, 'rb') as file:
            zoo = pickle.load(file)
        print(f"Данные зоопарка, загруженные из {filename}")
        return zoo
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return None

filename = 'zoo_data.pkl'
zoo = load_zoo(filename)
if zoo is None:
    zoo = Zoo()
    save_zoo(zoo, filename)

zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

zoo.add_employee(ZooKeeper("Вася"))
zoo.add_employee(Veterinarian("Петя"))

zoo.employees[0].feed_animal(bird)
zoo.employees[1].heal_animal(reptile)
