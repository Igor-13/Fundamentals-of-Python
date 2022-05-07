# Задача №1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
import hashlib


def sub_str(str_s):
    lst_1 = []
    lst_2 = []
    for len_sub in range(1, len(str_s)):
        for i in range(len(str_s) - len_sub + 1):
            h_sub = hashlib.sha1(str_s[i:i + len_sub].encode('utf-8')).hexdigest()
            if h_sub not in lst_1:
                lst_1.append(h_sub)
                lst_2.append(str_s[i:i + len_sub])

    if len(lst_2) > 0:
        return f'В строке "{str_s}" {len(lst_2)} различных подстрок: \n{lst_2}'
    return None


str_s = input('Введите строку состоящую только из маленьких латинских букв: ')
print(sub_str(str_s))
