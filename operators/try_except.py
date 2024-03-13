print('Start!')
# Oбработка исключений
# Операторы try...except

# Ошибки Errors - синтакс ошибки связанные с кодом
#     SyntaxError
#     IndentationError
#     TabError

# Исключения Exceptions -> связаны с неправильными данными которые передаются в код, операции
# ZeroDivisionError
# ArithmeticError
# NameError
# IndexError
# KeyError
# ValueError
# BaseException # прородитель всех исключений

# try:
#     num1 = int(input('Enter the number1: '))
#     num2 = int(input('Enter the number2: '))
#     print(f'{num1} / {num2} = {num1 / num2}')
# except:
#     print('Invalid Values!')

# print('Очень важный код')

# try:
#     num1 = int(input('Enter the number1: '))
#     num2 = int(input('Enter the number2: '))
#     print(f'{num1} / {num2} = {num1 / num2}')
# except ValueError:
#     print('Чувак ты ввел неправильные данные для фукнции int!')
# except ZeroDivisionError:
#     print('На ноль делить нельзя!')

# print('очень важная строчка кода!')
# --------------------------------

# try:
    # <body> # код с вероятным исключением
# except:
    # <body except> сработает только если ошибка в try
# <else>:
    # <body> сработает только если нет ошибки в try
# <finally>:
    # <body> сработает в любом случае

# dict_ = {1: 'one', 2: 'two', 3: 'three'}

# try:
#     key = int(input('Vvedite key: ')) 
#     print(dict_[key])
# except ValueError:
#     print('Invalid value for key!')
# except KeyError:
#     print('Key does not exists!')
# else:
#     print('No errors')
# finally:
#     print('The end!')

# ------------------------------------
# отображение ошибки
# 1. import sys
# import sys

# ls = [1,2,3,4,5]
# try:
#     index = int(input('Vvedite index: '))
#     print(ls[index])
# except:
#     print(f'Oops, we catched {sys.exc_info()[0]} error!')

# 2. Exception as <name(e)>

# ls = [1, 2, 3, 4, 5]
# while True:
#     try:
#         index = int(input('Vvedite index: '))
#         print(ls[index])
#     except Exception as e:
#         print(f'Oops, we catched {e.__class__} error!')







