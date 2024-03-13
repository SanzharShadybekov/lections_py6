# Области видимости и пространство имен (scopes)
# технология которая определяет контекст имени, в рамках которого мы можем ее использовать 

# a = 5
# def func():
#     b = 10
#     print(a) # 5
#     print(b) # 10

# func()
# print(b)

# built-ins(встроенная область видимости) - print(), len()
# global(глобальная) - область одного файла
# <enclosed>(замкнутая(не локальная, non local))
# local(локальная) -> область внутри одной функции

# human_peshkom = 10 # global
# len = 10
# print # buil-in

# def BMW(): #  global
#     human = 'Hello' # local
#     print(human_peshkom)
#     # print(a, 'local, inside in func!') # Hello

# print(a, 'global') # 10
# print(len)
# LEGB - local enclosed global built-in
        # ------->>>>>>>>

# ----------------------------------
# enclosed
# замкнутое пространсво имен - локальное пространство, у которого есть внутреннее(вложенное) локальное пространство 

# x = 'global'
# print(x, '1') # global

# def enclosed(): # global
#     x = 'enclosed'

#     def local(): # enclosed
#         x = 'local'
#         print(x, '3') # local
    
#     print(x, '2') # enclosed
#     local()
#     print(x, '4') # enclosed

# enclosed()
# print(x, '5') # global

# var = 0 

# def increment(): # LEGB 
#     global var
#     var = var + 1
#     if var < 15:
#         increment()


# increment()
# print(var)

# global -> позволяет изменять значение глобальной переменной внутри локальной области

# nonlocal -> позволяет изменять значение не локальной(замкнутой) переменной находясь внутри локальной области

# def counter(): #!!!!!!!!!!!!!!!!!!!!!
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment

# c_steps = counter()
# c_jumps = counter()

# print(c_steps)
# for _ in range(1, 10000):
#     c_steps()

# print(c_steps(), 'steps')
# print(c_jumps(), 'jumps')
# print(c_jumps(), 'jumps')
# print(c_jumps(), 'jumps')






