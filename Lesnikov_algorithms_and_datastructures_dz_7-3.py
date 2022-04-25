# Задача №3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве
# медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не
# меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это
# слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

import random


def median(lst, half):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]

    pivot = lst[0]

    less = []
    more = []
    pivots = []
    for item in lst:
        if item < pivot:
            less.append(item)
        elif item > pivot:
            more.append(item)
        else:
            pivots.append(item)

    if len(less) > half:
        return median(less, half)
    elif len(less) + len(pivots) > half:
        return pivots[0]
    else:
        return median(more, half - len(more) - len(pivots))


n = 6
temps = [random.randint(-100, 100) for _ in range(2 * n + 1)]
print(temps)
print(f'Медиана: {median(temps, n)}')
