# Реализация проекта «Операции с комплексными числами»

class Complex_number:

    def __init__(self, number_1):
        self.number_1 = number_1

    def __add__(self, other):
        self.number_1 = list(self.number_1)
        other.number_1 = list(other.number_1)
        return Complex_number(
            f'{int(self.number_1[0]) + int(other.number_1[0])} + {int(self.number_1[2]) + int(other.number_1[2])}{self.number_1[-1]}')

    def __mul__(self, other):
        self.number_1 = list(self.number_1)
        other.number_1 = list(other.number_1)
        return Complex_number(
            f'{int(self.number_1[0]) * int(other.number_1[0]) - int(self.number_1[2]) * int(other.number_1[2])} + {int(self.number_1[2]) * int(other.number_1[0]) + int(self.number_1[0]) * int(other.number_1[2])}{self.number_1[-1]}')

    def __str__(self):
        return f'Ответ: {self.number_1}'


x_1 = Complex_number('2+3i')
x_2 = Complex_number('2+3i')
print(x_1 * x_2)
