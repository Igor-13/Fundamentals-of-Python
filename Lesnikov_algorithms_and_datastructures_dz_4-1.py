# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых
# трех уроков. Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
# negative_number           my_func
# 0(n)                      0(n)
# 2.9 sec                   0.7 sec
# n = 15000000              n = 15000000
import time
from random import random


def time_of_func(func):
    def wrapper(*args):
        start_time = time.time()
        res = func(args)
        res_time = time.time() - start_time
        print('время исполнения = ', res_time)
        return res

    return wrapper


n = 15000000

list_num = []

for i in range(n):
    list_num.append(int(random() * 100) - 50)
# print(list_num)


@time_of_func
def negative_number(num):
    k = 0
    idx = -1
    while k < n:
        if list_num[k] < 0 and idx == -1:
            idx = k
        elif 0 > list_num[k] > list_num[idx]:
            idx = k
        k += 1
    print(f'Саммое отрицательное число: {list_num[idx]} под индексом {idx + 1}')


negative_number()


@time_of_func
def my_func(num_2):
    min_el = float('-inf')
    for item in list_num:
        if min_el < item < 0:
            min_el = item
    print('отрицательное число:', min_el)


my_func()
