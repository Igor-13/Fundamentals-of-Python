# Вывод элементов, значение которого больше предыдущего
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_values = []


def result_gen():
    idx_a = src[0]
    for idx_b in src:
        if idx_b > idx_a:
            idx_a = idx_b
            yield idx_b
        else:
            idx_a = idx_b


for values in result_gen():
    result_values.append(values)

print(result_values)
