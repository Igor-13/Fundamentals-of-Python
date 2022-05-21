# Задача №4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с
# клавиатуры.
n = int(input('Введите количество элемпентов: '))
x = 1
result = 0
sum_numb = 0
while n != 0:
    result = x / - 2
    sum_numb = sum_numb + result
    x = result
    n -= 1
print(sum_numb)
