# Реализация класса матрица
import random


class Matrix:

    def __init__(self, param, param_2):
        self.param = param
        self.param_2 = param_2

    def gen_mtx(self):
        mtx = []
        for i in range(self.param):
            x = []
            for j in range(self.param_2):
                y = random.randint(1, 100)
                x.append(y)
            mtx.append(x)
        return mtx

    def __str__(self):
        mtx = x.gen_mtx()
        for i in range(len(mtx)):
            for j in range(len(mtx)):
                print(mtx[i][j], end=' ')
            print()

    def __add__(self, other):
        rsl = []
        rsl_n = []
        mtx = x.gen_mtx()
        mtx_2 = other.gen_mtx()
        for i in range(len(mtx)):
            for j in range(len(mtx[0])):
                rsl_n.append(mtx[i][j] + mtx_2[i][j])
            rsl.append(rsl_n)
            rsl_n = []

        print(rsl)


x = Matrix(3, 3)
x_2 = Matrix(3, 3)
print(x.gen_mtx())
x.__str__()
x.__add__(x_2)


