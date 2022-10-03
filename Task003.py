# Задайте список из n чисел последовательности 
# (1+1/n)^n и выведите на экран их сумму.

number = int(input("Введите n: "))

result = {}
sum_number = 0

for key in range(1, number + 1):
    result[key] = round((1 + 1 / key)**key, 2)
    sum_number += result[key]

print(f'Итоговый список: {result}')  
print(f'Сумма: {round(sum_number, 3)}')