# Задача №6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import random

n = 10
list_num = [0] * n
for i in range(n):
    list_num[i] = int(random() * 50)
    print(list_num[i], end=' ')
print()

n_min = 0
n_max = 0
for i in range(1, n):
    if list_num[i] < list_num[n_min]:
        n_min = i
    elif list_num[i] > list_num[n_max]:
        n_max = i
print(f'Мин. значение: {list_num[n_min]} \nМакс. значение: {list_num[n_max]}')

if n_min > n_max:
    n_min, n_max = n_max, n_min

sum_n = 0
for i in range(n_min + 1, n_max):
    sum_n += list_num[i]
print(f'Сумма элементов: {sum_n}')
