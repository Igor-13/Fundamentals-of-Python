# Задача №3. По введенным пользователем координатам двух точек вывести уравнение
# прямой вида y=kx+b, проходящей через эти точки.

# пусть будет k = 2 и b = 2 тогда уравнение прямой будет равно y = 2x + 2
numb = int(input('Введите точку 1:'))
numb_2 = int(input('Введите точку 2:'))
point_1 = 2 * numb + 2
point_2 = 2 * numb_2 + 2
print(f'Прямая пройдёт через точку №1: (x = {numb}, а y = {point_1})'
      f' и точку №2: (x = {numb_2}, а y = {point_2})')