# Работа с файлами 

# Каретка - указатель - курсор

# open('путь до файла')
# file = open('files.py') # Относительный путь
# ~ working  -> Desktop/py.6/files/lections/files.py
# files working -> lections/files.py

# path = '/Users/sanzhar/Desktop/py.6/files/lections/files.py' # Абсолютный путь
# file = open(path, 'r')
# data = file.read()
# print(data, type(data))
# file.close()

# Режимы работы с файлами
# 1. r/r+/rb -> read - для чтения файлов
# 2. w/w+/wb -> write - для записи данных
# 3. a/a+ -> для добавления данных
# b, x 

# file = open('test.txt', 'r')
# print(file.read())
# file.close()

# file = open('test.txt', 'r')
# print(file.readlines())
# file.close()

# контекстный менеджер
# with open('test.txt', 'r') as file:
#     print(file.readline())
#     print(file.readline())
#     print('!!!!')
#     print(file.read())


# file.tell() - Возвращает индекс где находится каретка(указатель)
# file.seek() - Перемещает курсор на индекс который вы передали 
# with open('test.txt', 'r') as file:
#     print(file.tell()) # 0
#     data = file.read()
#     print(data, '!!')
#     print(file.tell())
#     file.seek(0)
#     data = file.read()
#     print(data, '!!')
#     print(file.tell())


# with open('test.txt', 'w') as file:
#     file.write('Hello world!\n')
#     file.write('My name is John Snow!\n')
#     file.write('I\'m Ned Starks bastard!\n')
#     # file.seek(0)
#     data = ['Test 1 stroka\n', 'Test 2 stroka']
#     file.writelines(data)


# with open('test.txt', 'a+') as f:
#     f.write('\nJohn Snow is a King of North!')
#     f.write('\nYou know nothing John Snow!')
#     f.seek(0)
#     print(f.read())

# -------------------------------------
# from PIL import Image
# import pytesseract
# import re


# base_url =  '/Users/sanzhar/Desktop/py.6/files/lections/'

# def get_imei_codes(image_path: str): 
#     string = pytesseract.image_to_string(image_path)
#     # print(string)
#     list_of_imei = re.findall(r'IMEI\d.\s\d+', string)
#     print(list_of_imei)

#     with open('imei_codes.txt', 'w') as file:
#         file.writelines(f'{x}\n' for x in list_of_imei)

# image_path = base_url + 'imei.jpg'
# get_imei_codes(image_path)




