# Задача №1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому
# из чисел в диапазоне от 2 до 9.

num = []
num_2 = [2, 3, 4, 5, 6, 7, 8, 9]
for i in range(2, 100):
    num.append(i)


def multiple(num_x, num_y):
    result = 0
    for idx in num_y:
        for z in num_x:
            if z % idx == 0:
                result += 1
        print(f' Для числа {idx} количество кратных {result}')
        result = 0


multiple(num, num_2)
