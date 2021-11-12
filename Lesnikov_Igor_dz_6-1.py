# Парсинг файла логов web-сервера
with open("nginx_logs.txt", 'r', encoding='utf-8') as fp:
    chunk_size = 256
    txt = fp.readline(chunk_size)
    while txt:
        txt_edit = str(txt)
        result = txt_edit.split(" ")
        tmp_line = f'{result[0]}, {result[5]}, {result[6]}'
        print(tmp_line)
        txt = fp.readline(chunk_size)



