# Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

number = int(input("Введите N: "))

new_list = []

for i in range(0, number):
    new_list.append(int(random.randint(- number, number)))
print(f'Список из {number} элементов: {new_list}') 

result = 1

f = open('file.txt', 'r')
for line in f:
    if line == "":
        break
    result *= new_list[int(line)]
f.close()
print(f'Произведение элементов (позиции элементов см. file.txt) = {result}')