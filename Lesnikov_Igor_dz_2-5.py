# Список цен
price = [25.4, 44.9, 85.13, 50, 74.4, 97.74, 81, 35.2, 10.48, 58.4, 44, 13.3, 11, 25.25, 78.7, 99, 66.6, 77.77, 55, 10.1]
# Сумматор цен
price_adder = []
# Цикл преобразования цен в рубли и копейки с добавлением в переменную enter
for cost_of_one in price:
    if type(cost_of_one) == float:
        cost_of_one = str(cost_of_one)
        meaning_all = cost_of_one.split('.')
        meaning_all_1 = meaning_all[0]
        meaning_all_2 = meaning_all[1]
        price_adder.append('{0} руб {1:02} коп, '.format(meaning_all_1, meaning_all_2))
    else:
        cost_of_one = str(cost_of_one)
        price_adder.append('{0} руб 00 коп, '.format(cost_of_one))
print(price_adder)
print(id(price_adder))
# Сортировка списка от меньшего к большему in place
price_adder.sort()
print(price_adder)
print(id(price_adder))
# Сортировка от меншего к большему с созданием нового объекта
price_adder = sorted(price_adder, reverse=True)
print(price_adder)
print(id(price_adder))
# Вывод 5-ти самых дорогих цен в порядке возростания
print(sorted(price_adder[0:5]))
print(id(price_adder))
