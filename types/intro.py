# Типы данных в питоне: 

# 1. NoneType - ничего, пустота -> None
# 2. Boolean - истинна или ложь -> True/False(1/0)
# 3. String - строки - str -> 'Hello world', "Hello world"
"My name is John Snow!"
'I\'m King of North'
"I'm King of North"
# 4. Числовые типы данных 
    # a) integer - int -> -1, 2, 555
    # b) float - число с плавающей точкой -> -1.5, 1.25
    # с) complex - 1.3j
# 5. Списковые типы данных (коллекция)
    # a) list(массив/список) -> [5, 3, 4, True, 'hello'] 
    # b) tuple(кортеж) -> (1, 2, 3, None)
    # c) range(последовательность) -> range(1, 10)
# 6. set() - множество -> {1, 2, 3, 4, 5}
# 7. dict(словари) -> содержат данные в себе в виде пары ключ значение {1: 'hello', 2: True, 3: 'John Snow'}
# ['hello', True, 'John Snow']

# ----------------------------------------
# Mutable(изменяемые типы данных)
# 1. list
# 2. set
# 3. dict

# Immutable(неизменяемые типы данных)
# 1. None
# 2. bool
# 3. int, float, complex
# 4. str
# 5. tuple, range
# 6. frozenset
# ------------------------------------

# переменная - проименованная область памяти, она прездназначена для хранения данных. С ее помощью мы можем проводить различные операции 

# PEP8 !!!


# listofnames = not recommended
# list_of_names = Snake case 
# listOfNames = Camel case

"""
Стандартный вывод данных
"""
# в питоне для вывода данных в терминал используется встроенная функция print()
# stroka = 'Hello world! My name is John Snow! Happy New Year!'
# print(stroka)
# print(1, 2, 3, 4, 5)

"""
стандартный ввод данных
используется функция input()
"""
# name = input('Enter your name: ') # John Snow
# print('Hello Mr/Mrs', name, end='!')

# str1 = input('Enter smt: ')
# print(str1)
# print(type(str1))

# num = 5
# print(num)
# print(type(num))

# num1 = input('Enter num1: ')
# num2 = input('Enter num2: ')
# num1 = int(num1)
# num2 = int(num2)
# print(num1, type(num1))
# print(num2, type(num2))
# print(num1 * num2)




