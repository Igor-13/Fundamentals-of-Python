# Задача №2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

from collections import Counter
import heapq


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def walk(self, codes, code):
        self.left.walk(codes, code + "0")
        self.right.walk(codes, code + "1")


class Val:
    def __init__(self, value):
        self.value = value

    def walk(self, codes, code):
        codes[self.value] = code
        return code


def huffman(str_s):
    lst = []

    for i, item in Counter(str_s).items():
        lst.append((item, len(lst), Val(i)))

    idx = len(lst)
    heapq.heapify(lst)
    while len(lst) > 1:
        x = heapq.heappop(lst)
        y = heapq.heappop(lst)
        heapq.heappush(lst, (x[0] + y[0], idx, Node(x[2], y[2])))
        idx += 1

    codes = {}
    if lst:
        lst[0][2].walk(codes, "")
    return codes


z = 'beep boop beer!'
print(f'строка из трех слов: \n{z}')
z = Counter(z)
print(z)
d = huffman(z)
print(d)
for key, value in d.items():
    print(f'{key}: {value}')