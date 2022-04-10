# Задача №9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import random

m_1 = 10
m_2 = 5
matrix = []
for i in range(m_2):
    matrix_x = []
    for j in range(m_1):
        matrix_z = int(random() * 200)
        matrix_x.append(matrix_z)
        print(matrix_z, end=' ')
    matrix.append(matrix_x)
    print()

matrix_q = -1
for j in range(m_1):
    matrix_w = 200
    for i in range(m_2):
        if matrix[i][j] < matrix_w:
            matrix_w = matrix[i][j]
    if matrix_w > matrix_q:
        matrix_q = matrix_w
print("Максимальный эелемент равен: ", matrix_q)
