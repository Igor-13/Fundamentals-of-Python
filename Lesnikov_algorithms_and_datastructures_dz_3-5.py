# Задача №5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import random

n = 15
list_num = []
for i in range(n):
    list_num.append(int(random() * 100) - 50)
print(list_num)

i = 0
idx = -1
while i < n:
    if list_num[i] < 0 and idx == -1:
        idx = i
    elif 0 > list_num[i] > list_num[idx]:
        idx = i
    i += 1

print(f'Саммое отрицательное число: {list_num[idx]} под индексом {idx + 1}')


