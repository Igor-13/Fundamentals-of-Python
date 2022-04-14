# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Первый - использовать алгоритм решето Эратосфена.
# Второй - без использования "решета". Проанализировать скорость и сложность алгоритмов.
# sieve                     simple_num
# 0(n**2)                   0(n**2)
# 0.8 sec                   0.06 sec
# n = 1500                  n = 1500
import time

n = int(input('Какое по счету простое число вы хотите найти: '))
lst = [i for i in range(n * n)]


def time_of_func(func):
    def wrapper(*args):
        start_time = time.time()
        res = func(*args)
        res_time = time.time() - start_time
        print('время исполнения = ', res_time)
        return res

    return wrapper


# Вариант 1. Решето Эратосфена.

@time_of_func
def sieve(num_list, idx):
    num_list[1] = 0
    i = 2
    s_num_list = []
    while len(s_num_list) < idx:
        if num_list[i] != 0:
            s_num_list.append(num_list[i])
            j = i * 2
            while j < len(num_list):
                num_list[j] = 0
                j += i
        i += 1
    return s_num_list[-1]


print(sieve(lst, n))

# Вариант 2. Без использования "решета".


@time_of_func
def simple_num(num_list, idx):
    num_list[1] = 0
    s_nums = []
    for i in range(2, len(num_list)):
        for num in s_nums:
            if num_list[i] % num == 0:
                break
        else:
            s_nums.append(num_list[i])
        if len(s_nums) == idx:
            return s_nums[-1]


print(simple_num(lst, n))
