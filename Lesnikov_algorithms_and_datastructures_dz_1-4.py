# 4. Написать программу, которая генерирует в указанных пользователем границах:
#   случайное целое число;
#   случайное вещественное число;
#   случайный символ.
#   Для каждого из трех случаев пользователь задает свои границы диапазона. Например,
#   если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа
#   должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random

numb_1 = float(input('Введите первое вещественное число: '))
numb_2 = float(input('Введите второе вещественное число: '))
print(f'Случайное число в данном интервале: {random.uniform(numb_1, numb_2)}')

numb_3 = int(input('Введите первое целое число: '))
numb_4 = int(input('Введите второе целое число: '))
print(f'Случайное число в данном интервале: {random.randint(numb_3, numb_4)}')


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

symbol_1 = alphabet.index(input('Введите первый символ: '))
symbol_2 = alphabet.index(input('Введите второй символ: '))


random_index = random.randint(symbol_1, symbol_2)

print(f'Случайный символ в данном интервале: {alphabet[random_index]}')
