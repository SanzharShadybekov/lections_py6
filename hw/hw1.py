'''
4) Напишите программу, которая генерирует первые n чисел в последовательности Фибоначчи, где n вводится пользователем.
'''
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 134 ....]
# 7
n = int(input('Введите n: '))
default = [0, 1]
if n <= 2:
    print(default)
else:
    i = 2
    while i < n:
        res = default[-1] + default[-2]
        default.append(res)
        i += 1
    print(default)





