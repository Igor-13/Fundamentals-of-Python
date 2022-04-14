# Задача №7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между
# собой (оба являться минимальными), так и различаться.

from random import random

n = 10
list_num = []
for i in range(n):
    list_num.append(int(random() * 100))
    print(list_num[i], end=' ')
print()

if list_num[0] > list_num[1]:
    min_n1 = 0
    min_n2 = 1
else:
    min_n1 = 1
    min_n2 = 0

for i in range(2, n):
    if list_num[i] < list_num[min_n1]:
        x = min_n1
        min_n1 = i
        if list_num[x] < list_num[min_n2]:
            min_n2 = x
    elif list_num[i] < list_num[min_n2]:
        min_n2 = i

print(f'Первое минимальное число находится под индексом: {min_n1} и равно: {list_num[min_n1]}')
print(f'Второе минимальное число находится под индексом:{min_n2} и равно: {list_num[min_n2]}')


