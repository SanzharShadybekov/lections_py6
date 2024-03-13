# zip(iterables) - она соединяет каждый элемент итерируемых объектов между собой в тип данных tuple и возвращает итератор

# ls1 = [1, 2, 3]
# ls2 = [100, 200, 300, 123]
# ls3 = ['hello', 'world', 'John']

# result = zip(ls1, ls2, ls3)
# print(list(result))
# for x in result:
#     print(x)

# -------------------------
# all(), any()

# all(Iterable) - Возращает True, если все элементы итерируемого объекта истина, иначе False

# ls = [[1,2], -5, 'stroka', 1, '']
# print(all(ls))

# ip1 = '10.255.12.155'
# ip2 = '10.255.1y.123'

# result = all(x.isdigit() for x in ip1.split('.'))
# print(result)

# result2 = all(x.isdigit() for x in ip2.split('.'))
# print(result2)

# any - Возвращает True, если хотябы один элемент истинна

# ls = [0, 0, '', None, [], 1]
# print(any(ls))

# ignore = ['rm -rf', 'sudo', 'reset', 'poweroff']

# command = input('Vvedite commandu: ') # sudo get system
# if any(x in command for x in ignore):
#     raise Exception('You don\'t have permissions!')

# print('OK!')

# Анонимные функции - lambda(обычные фукнции только без названия)
# lambda функции могуть принимать сколько угодно аргументов, но всегда возвращают одно выражение

# def sum_of_args(a, b):
#     return a + b

# print(sum_of_args(5, 6))

# func = lambda a, b: a + b
# print(func(15, 5))

# def myFunc(n):
#     return lambda num: num * n

# res = myFunc(4)

# myDoubler = myFunc(2)
# myTripler = myFunc(3)

# print(myDoubler(50))
# print(myDoubler(73))
# print(myDoubler(1111111111111))

# print(myTripler(55))

# dict_ = {'John': 1_000_000, 'Jamie': 100, 'Din': 10_000,
#         'Anvar': 500, 'Sam': 100_000}

# res = sorted(dict_.items(), key=lambda x: x[1], reverse=True)
# print(res)

# enumerate - она пронумеровывает каждый элемент внутри iterable, ее собсвенным индексом

# ls = ['hello', 'world', 'Din', 'Sam', 'Winchesters']
# print(ls)
# # res = list(enumerate(ls, 5))
# # print(res)
# for i, x in enumerate(ls):
#     print(f'Index: {i}, Element: {x}')

# -----------------------------------
# map(function, iterable) -> применяет фукнцию которую мы передаем ко всем элементам iterable

# ls = ['one', 'two', 'three', 'Anvar', 'King']
# res = list(map(str.upper, ls))
# print(res)

# res = []
# for x in ls:
#     res.append(x.upper())
# print(res)


# names = ['John', 'Sultan', 'Anvar', 'Din', 'Sam']
# res = list(map(
#     lambda name: f'Hello mr/mrs {name}!', names
# ))
# print(res)



# names = ['John', 'Sultan', 'Anvar', 'Din', 'Sam']
# def func(name):
#     return f'Hello mr/mrs {name}!'

# res = []
# for name in names:
#     res.append(func(name))

# print(names)
# print(res)

# dict_ = {1: 2, 3: 4, 5: 6}
# #   ---> {1: '2', 3: '4', 5: '6'}
# print(dict_)

# res = dict(map(
#     lambda x: (x[0], str(x[1])), dict_.items()
# ))
# print(res)


# filter(function, iterable) -> применяет ко всем элементам iterable функцию которую мы передали и возвращает итератор с теми элементами для которых фукнция вернула True 

# ls = ['one', 'two', '', 'list', '100', '12', 'din']
# # res = []
# # for x in ls:
# #     if x.isdigit():
# #         res.append(x)
# # print(res)
# res = list(filter(str.isdigit, ls))
# print(res)

# ls = ['john', 'codify', 'aibek', 'ono', 'bootcamp', 'Kyrgyzstan', 'mountains'] # > 5
# res = list(filter(lambda x: len(x) > 5, ls))
# print(res)


# ls = [
#     {'name': 'Python', 'point': 10},
#     {'name': 'C++', 'point': 6},
#     {'name': 'JS', 'point': 8},
#     {'name': 'JAVA', 'point': 3},
#     {'name': 'C#', 'point': 9},    
# ] # > 8

# res = list(filter(
#     lambda dict_: dict_['point'] > 8, ls     
# ))
# print(res)

# users = [
#     {'username': 'Din', 'comments': ['I love u!', 'so gorgeous!']},
#     {'username':'Raychel', 'comments':[]},
#     {'username':'Steven', 'comments':['Bishkek', 'Python']},
#     {'username':'Sam', 'comments':[]},
#     {'username':'Kira', 'comments':['The best post']}
# ]

# active_users = list(filter(
#     lambda obj: obj['comments'], users
# ))
# inactive_users = list(filter(
#     lambda obj: not obj['comments'], users
# ))
# print(active_users)
# print()
# print(inactive_users)

# -------------------
# names = ['Raychel', 'Sultan', 'Aigerim', 'John', 'Kira', 'Bob']

# res = list(
#     map(lambda x: f'Hello Mr/Mrs {x}', filter(lambda x: len(x) > 5, names))
# )
# print(res)

# ---------------------------
# Функция Reduce () принимает функцию и последовательность и возвращает одно значение, рассчитанное следующим образом:
# 1. Первоначально функция вызывается с первыми двумя элементами из последовательности, и результат возвращается.
# 2. Затем функция вызывается снова с результатом, полученным на шаге 1, и следующим значением в последовательности. Этот процесс повторяется до тех пор, пока в последовательности не закончатся элементы.

# from functools import reduce

# ls = [1, 2, 3, 4, 5]
# sum_ =  reduce(lambda x, y: x + y, ls)
# res = reduce(lambda a, b: a * b, ls)
# print(sum_, res)

# -------------------------------------
# from itertools import repeat
# from random import choices
# from string import ascii_letters, digits
# from statistics import mean

# symbols = '_()$!%+-@#'
# q_pass = int(input('Vvedite kol-vo paroley: '))

# result = {
#     f(choices(ascii_letters, k=10),
#       choices(digits, k=5), 
#       choices(symbols, k=2))
#     for f in repeat(
#         lambda a, d, s: ''.join(set(a+d+s)), q_pass)
# }
# print(result)
# print(f'Quantity of passwords: {len(result)}')
# dlina = [len(x) for x in result]
# print(f'Average len: {mean(dlina)}')










