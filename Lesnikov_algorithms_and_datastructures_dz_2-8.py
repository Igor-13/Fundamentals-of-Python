# Задача №8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество
# вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

n = int(input('Введите количество чисел: '))
m = int(input('Введите число которое надо посчитать: '))
numb = ''
for x in range(n):
    x = str(x + 1)
    numb = numb + x
z = 1
result = []
for i in range(0, len(numb), z):
    result.append(int(numb[i: i + z]))
total = 0
for k in result:
    if k == m:
        total += 1
print(total)
