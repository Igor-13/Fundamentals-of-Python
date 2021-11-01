# Список необходимых имён
names = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# Цикл, для извлечения и приведения к корректному виду имён
for retrieving_the_desired in names:
    retrieving_the_desired = retrieving_the_desired.split(' ')
    name = retrieving_the_desired[-1]
    print('Привет ' + name.capitalize())
