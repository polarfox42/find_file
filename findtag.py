#!/usr/bin/env python3
import os
import sys


def get_substring_and_directory():
    # arguments_for_search = sys.argv
    if len(sys.argv) < 2:
        print('Использование: findtag.py [слово для поиска] [адрес директории поиска, '
              'по умолчанию ищет в текущей] [адрес сохранения файла, по умолчанию сохраняет в директории поиска]')
        sys.exit()

    elif len(sys.argv) < 3:
        print('Для поиска и сохранения будет использована текущая директория.')
        return sys.argv[1], os.getcwd(), os.getcwd()

    elif len(sys.argv) < 4:
        print('Для сохранения будет использована директория поиска.')
        return sys.argv[1], sys.argv[2], sys.argv[2]

    return sys.argv[1], sys.argv[2], sys.argv[3]


def search_files(substring_for_search, directory_path):
    file_list = os.listdir(directory_path)
    result_file_list = []
    files = dict()

    for file in file_list:
        file_path = os.path.join(directory_path, file)
        if os.path.isfile(file_path) and substring_for_search in file:
            result_file_list.append(file)
            files[file] = ['file', file_path]
        elif os.path.isdir(file_path) and substring_for_search in file:
            result_file_list.append(file)
            files[file] = ('dir ', file_path)

    if len(result_file_list) == 0:
        return None, None

    print('Найдены следующие соответствия:')
    result_list = sorted(result_file_list)
    for i in range(len(result_list)):
        print(f'{i}. {result_list[i]}')
    return result_list, files


def create_file(result_list, files, directory_to_save):
    file_to_save = os.path.join(directory_to_save, 'files_found.txt')
    with open(file_to_save, 'w', encoding='utf-8') as save:
        for i in range(len(result_list)):
            save.write(f'{i}. {files[result_list[i]][0]} {files[result_list[i]][1]}\n')
    print('Операция завершена.')
    return files


def main() -> None:
    substring_for_search, directory_path, directory_to_save = get_substring_and_directory()
    result_list, files = search_files(substring_for_search, directory_path)
    if result_list is None:
        print('Ничего не найдено.')
    else:
        create_file(result_list, files, directory_to_save)


if __name__ == "__main__":
    main()
