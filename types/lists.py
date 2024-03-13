# list() - (списки, массив) - изменяемый, последовательный тип данны, который представляет из себя коллекцию каких либо объектов(элементы) внутри себя

# my_list = [1, 'string', 'hello', False, None, [1, 2, 3]]
# print(my_list, type(my_list))

# range() - возвращает последовательность чисел
# numbers = range(1, 101)
# print(numbers)
# ls = list(numbers)
# print(ls, type(ls))

# ls = list('Hello world')
# print(ls)

# Индексация в списках
# ls = [1, 2, 3, 4, 5, 'String', [[1,2,3], False, None], 5]
# print(ls, len(ls))
# print(ls[5], ls[-1])
# print(ls[6][0][1])
# print(ls[3:6])

# i = 0
# while i < 5:
#     print(i)
#     i += 1

# ls  = range(1, 11)
# for num in ls:
#     print(num)

# ls = ['John', 'Sansa', 'Tirion', 'Eddart', 'Jamie']
# # for x in ls:
# #     print(x)

# for x in ls:
#     print(f'Hello mr/mrs {x}! Welcome to the club!')

# for num in range(1, 21):
#     # print(num)
#     if num % 2 == 0:
#         print(f'Число {num} четное, квадрат: {num ** 2}')
#     else:
#         print(f'Число {num} нечетное, куб: {num ** 3}')

# -----------------------------

# методы списков
# print(dir(list))

# append(element) - Добавляет элемент в конец списка
# ls = [1, 2, 3]
# print(ls)
# ls.append(4)
# ls.append(5)
# ls.append('Hello')
# ls.append([True, False])
# print(ls)

# extend(container) - расширяет список

# ls = [1, 2, 3]
# ls.append('Hello')
# print(ls)
# ls.extend('Hello')
# print(ls)
# ls.extend([True, False])
# print(ls)

# ls = [1, 2, 3]
# ls1 = [4, 5, 6]
# print(ls + ls1)

# sort() - сортирует список, если передать reverse=True, то список отсортируется в убывающем порядке

# from random import randint

# ls = []
# for x in range(1, 101):
#     num = randint(1, 100)
#     ls.append(num)

# print(ls)
# ls = list(set(ls))
# ls.sort(reverse=False)
# print('After:\n', ls, len(ls))

# insert(index, element) - добавляет элемент по указанному index

# ls = ['string', 2, 3, False]
# print(ls)
# ls.insert(1, 1)
# ls.insert(4, 'Hello world')
# print(ls)

# remove(element) - удаляет element из списка, если такого нет, то выводится ошибка
# pop([index]) - удаляет и возвращает элемент из списка по index, но если index не передать, то удаляет последний элемент

# ls = [5, 1, 2, 4, 4, 5, 5, 5]
# print(ls)
# ls.remove(5)
# print(ls)
# while 5 in ls:
#     ls.remove(5)
# print(ls)
# ls.pop()
# ls.pop(0)
# print(ls)

# ls = [1, 2, 3]
# deleted = ls.pop()
# print(ls)
# print(deleted)

# update--------------
# ls = [1, 2, 't', 4, 5, 6, None, 8]
# ls[2] = 3
# print(ls)
# i = ls.index(None)
# ls[i] = 7
# print(ls)






