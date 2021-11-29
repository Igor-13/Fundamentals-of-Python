# Осуществление программы работы с органическими клетками, состоящими из ячеек

class Cell:

    def __init__(self, param_2):
        self.param = 15
        self.param_2 = param_2

    def __add__(self, other):
        if not isinstance(other, int):
            other = int(other)
        print(f'Сумма равна: {self.param + other}')

    def __sub__(self, other):
        if not isinstance(other, int):
            other = int(other)
        result = self.param - other
        if result <= 0:
            print('Некорректное число. Введите положительно число.')
        else:
            print(f'Разность равна: {result}')

    def __mul__(self, other):
        if not isinstance(other, int):
            other = int(other)
        print(f'Произведение равно: {self.param * other}')

    def __floordiv__(self, other):
        if not isinstance(other, int):
            other = int(other)
        print(f'Деление равно: {self.param // other}')

    def make_order(self):
        number = ''
        idx = 0
        idx_2 = self.param_2
        for _ in range(self.param):
            if idx < idx_2:
                number += '*'
                idx += 1
            else:
                number += '\n*'
                idx = 1
        print(number)


a = Cell(2)
a.__add__(a.param_2)
a.__sub__(a.param_2)
a.__mul__(a.param_2)
a.__floordiv__(a.param_2)
a.make_order()
