# Задача №1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована
# в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

import random


def bubble_sort(array):
    rev = True
    if rev:
        left = 1
        right = 0
    else:
        left = 0
        right = 1
    n = 1
    length = len(array)
    while n < length:
        count = True
        for i in range(n - 1, length - n):
            if array[i + left] > array[i + right]:
                array[i], array[i + 1] = array[i + 1], array[i]
                count = False
        if count:
            break
        for j in range(length - n, n - 1, -1):
            if array[j - left] < array[j - right]:
                array[j], array[j - 1] = array[j - 1], array[j]
        n += 1


temps = [random.randint(-100, 99) for x in range(10)]
print(temps)
bubble_sort(temps)
print(f'Отсортированный список: {temps}')
