# Задача №4. Определить, какое число в массиве встречается чаще всего.

from random import random

n = 15
list_num = [0] * n
for i in range(n):
    list_num[i] = int(random() * 20)
print(list_num)

number = list_num[0]
max_num = 1
for i in range(n - 1):
    idx = 1
    for k in range(i + 1, n):
        if list_num[i] == list_num[k]:
            idx += 1
    if idx > max_num:
        max_num = idx
        number = list_num[i]

if max_num > 1:
    print(f'Число {number} встречается {max_num} раз(а)')
else:
    print('Все элементы уникальны')


