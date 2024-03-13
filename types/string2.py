# text = 'The more you learn, the more you earn.' 
# # len() - возвращает длину строки, считая каждый ее символ
# len_text = len(text)  # 38
# print(text, len_text)
# print(text[::-1])

# count_e = 0
# i = 0
# while i < len_text:
#     symbol = text[i]
#     if symbol == 'e' or symbol == 'E':
#         count_e += 1
#     print(symbol)
#     i += 1 # инкремент i = i + 1

# print(f'Symbol E is found: {count_e} times!')

# Custom len code 
# text = 'The more you learn, the more you earn.' 
# count_e = 0
# i = 0
# c = 0
# while text[i:]:
#     i += 1
#     c += 1
#     print(c)

# ---------------------------------

# Методы строк - dir()

# print(dir('123'))

# count(value, [start]) - считает кол-во вхождений value в нашу строку
# text = 'hello  o o o o hello'
# print(text.count('o'))
# print(text.count('h', 5))
# print(text.count('hello'))

# replace(old, new, [count]) - меняет в строке old символ на new, заменит count раз если передаете число
# text = 'ha ha ha ha'
# res = text.replace('ha', 'xa', 2)
# print(f'original: {text}')
# print(f'result after replace: {res}')

# strip() - Убирает пробельные символы в начале и в конце строки
# rstrip, lstrip
# a = '   Hello   '
# print(a, len(a), sep='->')
# res = a.strip()
# print(res, len(res), sep='->')
# print(a.lstrip(), '1')

# print(dir(str))

# isdigit -         Проверяют
# isnumeric -  состоит ли наша строка
# isdecimal -   полностью из чисел

# num = input('Vvedite chislo: ')
# print(f'Vvedeno li chislo?: {num.isdigit()}')

# isalpha - состоит ли наша строка из символов алфавита 
# txt = 'Hello world'
# print(txt.isalpha())
# res = txt.replace(' ', '')
# print(res, res.isalpha())

# num = input('Vvedite chislo: ')
# if num.isdigit(): 
#     num = int(num)
#     print(f'{num} * 5 = {num * 5}')
# else:
#     print('Vy vveli ne chislo!')

# split(separator) - дробит(разделяет) строку на несколько частей по разделителю, все части сохраняются в типе list

# text = 'Let me speak in English!'
# res = text.split('e')
# print(text)
# print(res)
# print(text.split())

# a = '#hello#life#work#love#bishkek'
# print(a)
# print(a[1:].split('#'))

# 'connector'.join(list) - соединяет по connector строкие которые были в list
# ls = ['Anvar', 'John', 'Jamie', 'Osmon']
# print(ls)
# res = '-->'.join(ls)
# print(res)

# swapcase() - переводит все символы в противоположный регистр
# upper() - переводит все в верхний регистр
# lower() - переводит все в нижний регистр

# text = 'Hello WorLD, JOHN snow'
# print(f'Original: {text}')
# print(text.swapcase())
# print(text.upper())
# print(text.lower())

# index(value) - выводит индекс значения value внутри строки
# find(value) - делает тоже самое что и index, но если не нашел value то вернется -1

# text = 'Hello John Snow'
# print(text.index('o'))
# print(text.index('John'))
# print(text.index('o', -2))
# print(text.find('a'))



