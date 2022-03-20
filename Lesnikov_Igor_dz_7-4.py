#  Cкрипт, который выводит статистику для заданной папки в виде словаря
import os

folder = 'some_data'
size_file = [100, 1000, 10000, 100000]

small_files_1 = [item.name
                 for item in os.scandir(folder)
                 if item.stat().st_size < size_file[0]]
small_files_2 = [item.name
                 for item in os.scandir(folder)
                 if size_file[0] < item.stat().st_size < size_file[1]]
small_files_3 = [item.name
                 for item in os.scandir(folder)
                 if size_file[1] < item.stat().st_size < size_file[2]]
small_files_4 = [item.name
                 for item in os.scandir(folder)
                 if size_file[2] < item.stat().st_size < size_file[3]]
dictionary_size = [small_files_1, small_files_2, small_files_3, small_files_4]
statistics_dict = {

}


def folder_size():
    idx = 0
    for key in size_file:
        val = len(dictionary_size[idx])
        for_dict = {key: val}
        statistics_dict.update(for_dict)
        idx += 1


folder_size()
print(statistics_dict)
