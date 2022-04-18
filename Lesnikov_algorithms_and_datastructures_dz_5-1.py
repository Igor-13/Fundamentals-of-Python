# Задача №1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
import collections

while True:
    try:
        company = int(input('Введите данные о количестве компаний: '))
    except ValueError:
        print('Ваше значение не корректно, попробуйте ещё раз!')
        continue
    break

comp_all = collections.defaultdict()
above_average = collections.deque()
below_average = collections.deque()
all_profit = 0
quarter = 4

for i in range(company):
    name = input(f'Наименование компании {i + 1}: ')
    profit = 0
    idx = 1
    while idx <= quarter:
        try:
            profit += float(input(f'Прибыль компании {name} за {idx}й квартал: '))
        except ValueError:
            print('Ваше значение не корректно, попробуйте ещё раз!')
            continue
        idx += 1
    comp_all[name] = profit
    all_profit += profit

average_profit = all_profit / company
for i, item in comp_all.items():
    if item >= average_profit:
        above_average.append(i)
    else:
        below_average.append(i)
print(f'Средняя прибыль компаний составляет: {average_profit}')
print(f'Прибыль выше среднего значения у {len(above_average)} компаний:')
for name in above_average:
    print(name)
print(f'Прибыль ниже среднего значения у {len(below_average)} компаний:')
for name in below_average:
    print(name)

# Сложность алгоритма: 0(n)
