# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


symbol = int(input('Введите позицию буквы: ')) - 1
letter = alphabet[symbol]
print(f'Вы ввели позицию буквы: {letter}')
