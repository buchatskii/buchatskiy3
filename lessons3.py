# 1. Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

# list = [random.randint(0, 10) for i in range(random.randint(3, 10))]
# sumAll = 0
# n = 1
# while(n < len(list)):
#     sumAll = sumAll + list[n]
#     n = n + 2
# print(f"Сформированный список:\n{list}" "->" f"Cумму элементов на нечётной позиции = {sumAll}")

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний
# элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16]
# - [2, 3, 5, 6] => [12, 15]


# list = [random.randint(0, 8) for i in range(random.randint(3, 8))]
# print(f"Сформированный список:\n{list}")
# n = 0
# array = []
# while(n < (len(list) / 2)):
#     array.append(list[n] * list[len(list) - (n + 1)])
#     n += 1
# print(array)


# 3. Задайте список из вещественных чисел. Напишите программу,
#  которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# list = [round(random.random() * random.randint(0, 50), 2) for i in range(random.randint(3, 10))]
# print(f"Заданный список:\n{list}")
# array = []
# i = 0
# while(i < len(list)):
#     array.append((round(list[i] % 1,2)))
#     i += 1
# print(f"Минимальное значение дробной части заданного списка:\n{round(max(array) - min(array), 2)}")


# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# fibona = int(input('Введите число: '))
# def get_fibonacci(n):
#     fibo_num = []
#     a, b = 1, 1
#     for i in range(n - 1):
#         fibo_num.append(a)
#         a, b = b, a + b
#     a, b = 0, 1
#     for i in range (n):
#         fibo_num.insert(0, a)
#         a, b = b, a - b
#     return fibo_num
# print(get_fibonacci(fibona + 1))