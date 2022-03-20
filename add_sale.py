# Скрипт для записи данных
import sys

args_add = sys.argv[1:]
sale = '5978,5 8914,3 7879,1 1573,7'
with open('bakery.csv', 'w', encoding='utf-8') as f:
    f.writelines(sale)
