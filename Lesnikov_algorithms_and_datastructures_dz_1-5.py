# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

symbol_1 = alphabet.index(input('Введите первый символ: '))
symbol_2 = alphabet.index(input('Введите второй символ: '))

place_1 = symbol_1 + 1
place_2 = symbol_2 + 1
if place_1 < place_2:
    number_of_letters = place_2 - place_1 - 1
else:
    number_of_letters = place_1 - place_2 - 1

print(f'Первый символ стоит на {place_1} месте, второй символ на '
      f'{place_2} месте, а между ними {number_of_letters} букв')