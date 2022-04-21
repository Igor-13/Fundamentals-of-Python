# Задача №2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
import collections
from copy import deepcopy

sixteen_str = '0123456789ABCDEF'
sixteen_table = collections.defaultdict(int)
int_table = collections.defaultdict(int)
for idx, item in enumerate(sixteen_str):
    sixteen_table[item] = idx
    int_table[idx] = item


class SixteenError(BaseException):
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f'{self.num} - значение не допустимо'


class SixteenNum:
    table_s = sixteen_table
    table_int = int_table

    def __init__(self, num):
        try:
            self.num = collections.deque()
            for item in num:
                self.num.append(item.upper())
                if item.upper() not in self.table_s:
                    raise SixteenError(item)
        except TypeError:
            print('SixteenNum использует только итерируемые объекты!')

    def __str__(self):
        s = 's: '
        for i in self.num:
            s += i
        return s

    def __add__(self, other):
        try:
            if len(other.num) > len(self.num):
                a = deepcopy(other.num)
                b = deepcopy(self.num)
            else:
                a = deepcopy(self.num)
                b = deepcopy(other.num)
        except AttributeError:
            print("Возможно сложение только шестнадцатеричных чисел")
            raise SystemExit
        temp = 0
        result = collections.deque()
        for n in range(len(a)):
            first = self.table_s[a.pop()]
            if len(b) != 0:
                second = self.table_s[b.pop()]
            else:
                second = 0
            temp_res = first + second + temp
            if temp_res > 15:
                temp = 1
            else:
                temp = 0
            temp_res %= 16
            result.appendleft(self.table_int[temp_res])
        if temp != 0:
            result.appendleft(self.table_int[temp])
        result = SixteenNum(result)
        return result

    def __mul__(self, other):
        try:
            z = deepcopy(self.num)
            x = deepcopy(other.num)
        except AttributeError:
            print("Возможно умножение только шестнадцатеричных чисел")
            raise SystemExit
        dec = 0
        answer = SixteenNum('0')
        result = collections.deque()
        for i in range(len(z) - 1, -1, -1):
            temp = 0
            for j in range(len(x) - 1, -1, -1):
                temp_res = self.table_s[z[i]] * self.table_s[x[j]] + temp
                if temp_res > 15:
                    temp = temp_res // 16
                else:
                    temp = 0
                temp_res = temp_res % 16
                result.appendleft(self.table_int[temp_res % 16])
            if temp != 0:
                result.appendleft(self.table_int[temp])
            for d in range(dec):
                result.append('0')
            result = SixteenNum(result)
            answer += result
            result = collections.deque()
            dec += 1
        return answer

    __rmul__ = __mul__


a = SixteenNum('c5')
b = SixteenNum('A3B')
c = SixteenNum('CF24A')
d = SixteenNum('64CF')
e = SixteenNum('ABF')
f = SixteenNum('CDE')
print('Сумма a + b равна', a + b)
print('Произведение a * b равно', a * b)
print('Сумма c + d равна', c + d)
print('Произведение c * d равно', c * d)
print('Сумма e + f равна', e + f)
print('Произведение e * f равно', e * f)


# Сложность алгоритма: 0(n**2)