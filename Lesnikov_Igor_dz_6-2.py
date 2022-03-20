# Код формирующий словарь: ключи — ФИО, значения — данные о хобби
with open("users.csv", 'r', encoding='utf-8') as fp:
    chunk_size = 256
    txt = fp.readline(chunk_size)
    list_txt = []
    while txt:
        txt_edit = str(txt)
        result = txt_edit.split(",")
        x_dict = f'{result[0]} {result[1]} {result[2]}'
        list_txt.append(x_dict)
        txt = fp.readline(chunk_size)

with open("hobby.csv", 'r', encoding='utf-8') as fph:
    chunk_size = 256
    txt_2 = fph.readline(chunk_size)
    list_txt_2 = []
    while txt_2:
        txt_2_dict = str(txt_2)
        list_txt_2.append(txt_2_dict)
        txt_2 = fph.readline(chunk_size)

with open("dictionary.txt", 'r+', encoding='utf-8') as fpd:
    dict_n = {}
    idx = 0
    while idx < len(list_txt):
        if len(list_txt) > len(list_txt_2):
            list_txt_2.append('None')
        elif len(list_txt) < len(list_txt_2):
            print('"1"')
            break
        else:
            dict_n.setdefault(list_txt[idx], list_txt_2[idx])
            idx += 1
            name = str(dict_n)
            fpd.write(name)
            print(fpd.read())


