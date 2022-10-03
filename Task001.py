# Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = float(input("Введите число: "))

if number < 0:
    number = abs(number) # Функция abs() возвращает модуль числа

sum_number = 0    
number_str = str(number)
for i in number_str:
    if i != '.':
        sum_number += int(i) 

print(sum_number)  