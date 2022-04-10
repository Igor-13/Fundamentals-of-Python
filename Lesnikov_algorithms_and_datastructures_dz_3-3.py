# Задача №3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

num = list(input('Введите числа: '))
min_num = min(num)
max_num = max(num)
idx_min = num.index(min_num)
idx_max = num.index(max_num)
num[idx_min] = max_num
num[idx_max] = min_num
print(num)


