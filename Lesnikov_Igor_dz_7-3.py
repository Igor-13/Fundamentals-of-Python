# Cкрипт, который выводит статистику для заданной папки в виде словаря
import os
import shutil

folder = os.path.join('my_project', 'templates')
if not os.path.exists(folder):
    os.mkdir(folder)
all_path = []
all_dirs = []
all_files = []
for path, dirs, files in os.walk('my_project'):
    all_path.append(path)
    for dirs_name in dirs:
        all_dirs.append(dirs_name)
    for files_name in files:
        all_files.append(files_name)
idx = 0
while idx < len(all_dirs):
    try:
        folder_2 = os.path.join(folder, all_dirs[idx])
        if not os.path.exists(folder_2):
            os.mkdir(folder_2)
            shutil.copy2(os.path.join(all_path[idx+1], all_files[idx]), os.path.join(folder_2, all_files[idx]))
            shutil.copy2(os.path.join(all_path[idx + 1], all_files[idx]), os.path.join(folder_2, all_files[idx+1]))
            idx += 1
        else:
            idx += 1
    except OSError as e:
        idx += 1
        print(f'OS says: {e}')
