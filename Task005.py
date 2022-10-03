# Реализуйте алгоритм перемешивания списка.

import random

lst = []

for i in range(5):
    lst.append(random.randint(-10, 10))

print(f"Исходный список: {lst}")

random.shuffle(lst)

print(f"Список после перемешивания: {lst}")