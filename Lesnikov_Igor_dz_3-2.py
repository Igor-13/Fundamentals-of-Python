# Функция возвращающая словарь с именами сотрудников
def thesaurus_adv(*all_names, **kwargs):
    names_scroll = list(all_names)
    for val in names_scroll:
        key = val[0]
        if key in kwargs:
            kwargs[key].append(val)
        kwargs.setdefault(key, [val])
    return kwargs


print(thesaurus_adv('Игорь', 'Алина', 'Роман', 'Илья', 'Диана', 'Дарья', 'Анастрезультатасия'))
