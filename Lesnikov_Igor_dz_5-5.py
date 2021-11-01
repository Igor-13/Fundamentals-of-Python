# Определение элементов не имеющих повторений
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []


def result_gen():
    new_list = []
    for idx_a in src:
        for idx_b in range(len(src)):
            if src[idx_b] == idx_a:
                new_list.append(idx_a)
        if new_list.count(idx_a) > 1:
            None
        else:
            yield idx_a


for unique_value in result_gen():
    result.append(unique_value)

print(result)
