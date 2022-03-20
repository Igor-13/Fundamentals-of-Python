#  Cкрипт, создающий стартер (заготовку) для проекта папок:
import os

folder = 'my_project'
if not os.path.exists(folder):
    os.mkdir(folder)

folder_name = ['settings', 'mainapp', 'adminapp', 'authapp']
try:
    for dir_folder in folder_name:
        dir_way = os.path.join(folder, dir_folder)
    if os.path.exists(dir_way):
        os.makedirs(dir_way)
except OSError as e:
    print(f'OS says: {e}')
