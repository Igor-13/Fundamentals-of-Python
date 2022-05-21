# Задача №9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это
# число и сумму его цифр.

n = None
numb = []
while n != 0:
    n = int(input('Введите следующее число. Если больше вводить числа не будете, то введите "0": '))
    if n != 0:
        numb.append(n)
    else:
        break
print(numb)
z = 1
total = 0
total_numb = 0
for x in numb:
    x = str(x)
    for i in range(0, len(x), z):
        total = total + i
    if total_numb < total:
        total_numb = total
    else:
        continue
print(total_numb)
