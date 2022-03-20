# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

numb = int(input('Введите первое число: '))
numb_2 = int(input('Введите второе число: '))
numb_3 = int(input('Введите третье число: '))

if numb_2 < numb < numb_3:
    print(f'Число {numb} является средним!')
elif numb_3 < numb < numb_2:
    print(f'Число {numb} является средним!')
elif numb < numb_2 < numb_3:
    print(f'Число {numb_2} является средним!')
elif numb_3 < numb_2 < numb:
    print(f'Число {numb_2} является средним!')
elif numb < numb_3 < numb_2:
    print(f'Число {numb_2} является средним!')
else:
    print(f'Число {numb_3} является средним!')
