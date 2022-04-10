# Задача №8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять
# сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести
# полученную матрицу.

m_1 = 5
m_2 = 4
matrix = []
for i in range(m_2):
    matrix_x = []
    matrix_z = 0
    print(f'{i}-я строка: ')
    for j in range(m_1 - 1):
        k = int(input())
        matrix_z += k
        matrix_x.append(k)
    matrix_x.append(matrix_z)
    matrix.append(matrix_x)

for i in matrix:
    print(i)


