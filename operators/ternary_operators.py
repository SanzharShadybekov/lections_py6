# sentence = input('Vvedite predlojeniye: ')

# res = 'Yes, voprositel\'noye!' if sentence[-1] == '?' else 'Normal one'
# print(res)

# if sentence[-1] == '?':
#     print('Yes, voprositel\'noye!')
# else:
#     print('Normal one')

# Ternary operators(Тернарный оператор) - это конструкция которая по своему дейтвию аналогична конструкции if/else, но при этом записывается в одну строчку

# num = int(input('Vvedite chislo: '))
# print('even number' if num % 2 == 0 else 'odd number')
#      четное                               нечетное

# ls = [55, 65, 75, 89, 100, 15, 6]
# print(ls)
# choice = input('Vvedite max/min: ').lower().strip()
# res = max(ls) if choice == 'max' else min(ls) if choice == 'min' else 'Invalid operator!'
# print(res)

# ---------------------------------------------
flag = True
symbols = '0123456789' + '-' + '.' 

while flag:
    print() 
    num1 = input('Введите первое число: ') # 12.12
    is_corrent = True
    for x in num1:
        if x not in symbols:
            print('Вы ввели некорректное число!')
            is_corrent = False
            break
    if not is_corrent:
        continue

    num2 = input('Введите второе число: ') # 12.12
    is_corrent = True
    for x in num2:
        if x not in symbols:
            print('Вы ввели некорректное число!')
            is_corrent = False
            break
    if not is_corrent:
        continue

    num1 = float(num1) if '.' in num1 else int(num1)
    num2 = float(num2) if '.' in num2 else int(num2)

    # print(num1, type(num1))
    # print(num2, type(num2))
    operator = input('Введите операцию(+,-,*,/): ').strip()
    if operator == '+':
        print(f'Результат: {num1 + num2}')
    elif operator == '-': 
        print(f'Результат: {num1 - num2}')
    elif operator == '*': 
        print(f'Результат: {num1 * num2}')
    elif operator == '/': 
        print(f'Результат: {num1 / num2}' if num2 != 0 else 'На ноль делить нельзя!')
    else:
        print('Вы ввели неверный оператор!')

    choice = input('Хотите продолжить(yes/no)?: ')
    if choice.lower().strip() != 'yes':
        flag = False
        print('Пока пока!')





