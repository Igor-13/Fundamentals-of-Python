# Функция которая извлекает имя пользователя и почтовый домен
import re
txt = 'someone@geekbrains.ru'
RE_PRODUCTS = re.compile(r'(?P<username>.+)@(?P<domain>\w+[.?]\w+)')

try:
    user = RE_PRODUCTS.search(txt)
    user = user.groupdict()
    print(user)
except AttributeError as e:
    print(f'{e}: wrong email: {txt}')

