# Список для обработки
different_meanings = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
idx = 0
# Цикл вычесления и обособления чисел с добавлением нулём до двух целочисленных разрядов
while idx < len(different_meanings):
    meaning = different_meanings[idx]
    if meaning.isdigit():
        numerical_value = meaning
        value_index = different_meanings.index(numerical_value)
        different_meanings.remove(numerical_value)
        different_meanings.insert(value_index, '"')
        different_meanings.insert(value_index, '{:>02}'.format(numerical_value))
        different_meanings.insert(value_index, '"')
        idx += 3
    elif meaning.count('+') > 0:
        numerical_value = meaning
        value_index = different_meanings.index(numerical_value)
        different_meanings.remove(numerical_value)
        numerical_value = numerical_value.split('+')
        numerical_value = numerical_value[1]
        different_meanings.insert(value_index, '"')
        different_meanings.insert(value_index, '+{:>02}'.format(numerical_value))
        different_meanings.insert(value_index, '"')
        idx += 3
    elif meaning.count('-') > 0:
        numerical_value = meaning
        value_index = different_meanings.index(numerical_value)
        different_meanings.remove(numerical_value)
        numerical_value = numerical_value.split('-')
        numerical_value = numerical_value[1]
        different_meanings.insert(value_index, '"')
        different_meanings.insert(value_index, '-{:>02}'.format(numerical_value))
        different_meanings.insert(value_index, '"')
        idx += 3
    else:
        idx += 1
print(' '.join(different_meanings))
