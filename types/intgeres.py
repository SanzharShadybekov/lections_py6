# Типы данных числа -> int, float

# = -> оператор присваивания
# num = 5
# print(num) # 5
# num = 79 # переопределение
# print(num) # 79
# num += 1 # num = num + 1
# print(num) # 80
# num -= 5
# print(num)

# abc -> нижний регистр
# ABC -> верхний региср

# PEP8
# tomorrow_day = '11.01.2024' # Snake case
# tomorrowDay = '11.01.2024' # Camel case

# +
# num1 = 5
# num2 = 15
# result = num1 + num2
# print(result)

# -
# num1 = int(input('Enter the num1: '))
# num2 = int(input('Enter the num2: '))
# print(num2, '-', num1, '=', num2 - num1)

# *
# num1 = int(input('Enter the num1: '))
# num2 = int(input('Enter the num2: '))
# print(num2, '*', num1, '=', num2 * num1)

# / and // and %
# / - обычное деление
# // - деление без остатка
# % - модульное деление (получение остатка от деления)

# num1 = 17
# num2 = 5
# print('/', num1 / num2)
# print('//', num1 // num2)
# print('%', num1 % num2)

# ** -> возведение в степень

# print(5 ** 2)
# print(17 ** 55)

# print(144 ** (1/2)) # квадратный корень
# print(36 ** -2)

# res = 5 * (15 + 5)
# print(res)

# pow - возведение в степень
# pow(num1, num2, <mod>)
# print(pow(5, 2)) # 5 ** 2
# print(pow(5, 2, 2)) # 5 ** 2 % 2

# a = 6 
# c = 3
# res = pow(a, c, 50)
# print(res)

# abs() - абсолютное значение цисла -> abs(-5) -> 5
                                        # |-5| -> 5

# a = abs(-16)
# b = abs(15)
# c = abs(-2.5)
# print(a, b, c)

# round() - округление числа с плавающей точкой
# a = 5.37
# print(round(a))

# b = 7.368232
# print(round(b, 1))

# divmod(a, b) - она выводит два числа, первое число это результат целого деления(//), а второе число это модульное деление чисел a и b

# print(22 / 5) # 4.4
# print(divmod(110, 7))

# import math

# a = 5
# print(round(math.sqrt(5), 1))

# множественное присваивание
# a = 'moloko' 
# b = 'voda'
# c = None

# c = b
# b = a
# a = c
# print(a, b)

# a = 'moloko' 
# b = 'voda'
# a, b = b, a
# print(a, b)

# num1, num2, num3 = input('num1: '), input('num2: '), input('num3: ')
# print(num1)
# print(num2)
# print(num3)


"""
13) Даны 2 катета прямоугольного треугольника. Рассчитайте длину его гипотенузы, воспользовавшись теоремой Пифагора.
"""
# import math 

# katet1 = 5
# katet2 = 6

# res = math.sqrt(katet1 ** 2 + katet2 ** 2)
# print(round(res, 2))

"""
Дана переменная с радиусом окружности, найдите периметр и площадь окружности, результат выведите в терминал
"""
# from math import pi

# r = int(input('Vvedite radius: '))
# resP = 2 * r * pi
# resS = r ** 2 * pi
# print('S okruzhnosti: ', round(resS, 2))
# print('P okruzhnosti: ', round(resP, 2))

# from random import randint

# num = randint(1, 10) # 5
# print(num)
# i = 0
# while i < 3:
#     guess = int(input('Ugadai chislo: ')) # 5
#     if guess == num:
#         print('Ty pobedil! Gratz!')
#         i = 3
#     i += 1



from random import uniform
for x in range(1, 100):
    num = round(uniform(1, 10), 1)
    print(num)

