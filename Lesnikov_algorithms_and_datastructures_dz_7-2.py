# Задача №2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

temps = [round(random.uniform(0, 49.99), 2) for x in range(10)]


def merge_sort(lst):

    if len(lst) <= 1:
        return lst

    left_side = merge_sort(lst[:len(lst) // 2])
    right_side = merge_sort(lst[len(lst) // 2:])

    i = j = 0
    result = []

    while i < len(left_side) or j < len(right_side):

        if i >= len(left_side):
            result.append(right_side[j])
            j += 1

        elif j >= len(right_side):
            result.append(left_side[i])
            i += 1

        elif left_side[i] < right_side[j]:
            result.append(left_side[i])
            i += 1

        else:
            result.append(right_side[j])
            j += 1

    return result


print(temps)
print(f'Отсортированный список: {merge_sort(temps)}')