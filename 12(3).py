import os

current_path = os.path.abspath(__file__)#абсолютный путь до этого файла, в котором сейчас работаем
parent_path = os.path.join(current_path, '..','..')

# print(current_path)
# print(parent_path)

#рекурсия
# def recurs(count):
#     print(count)
#     if count == 5:
#         return
#     recurs(count+1)
#     print(count)
# recurs(0)

def get_all_files(path):
    for i_name in os.listdir(path):
        new_path = os.path.join(path, i_name)
        if os.path.isdir(new_path):
            print('asd',i_name)
            get_all_files(new_path)
        else:
            print('-',i_name)

get_all_files(parent_path)