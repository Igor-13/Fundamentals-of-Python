# Генератор возвращающий картежи вида (<tutor>, <klass>)
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', "Екатерина", "Виктория"
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def view_gen():
    for i in range(len(tutors)):
        if i < len(klasses):
            name_klass = (tutors[i], klasses[i])
        else:
            name_klass = (tutors[i], 'None')
        yield name_klass


for result in view_gen():
    print(result)

print(type(view_gen()))
