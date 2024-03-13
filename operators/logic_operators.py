# Операторы сравнения
# Условные операторы
# Логические операторы

# операторы сравнения
# <, >, ==(равно), !=(не равно), <=, >=

# 1 > 5 --> False
# 7 < 9 --> True

# print('ABC1234124' > 'abc123')

# 1 2 4 8 16 32 64 128 256 512 1024 2048 
# 0  0  1 0   1  
# 0  0  1  1  0 1
# 1  1 1  1
# 44 --> 101100
# 15 --> 1111
# 20 -->  10100

# a = 'A'
# b = 'b'
# print(ord(a), ord(b))
# num = 1100
# print(chr(num))

# Условные операторы
# if 
# elif
# else

# if <condition>:
#     <body if> #сработает если в condition if придет True
# [elif] <condition>:
#     <body elif>
# [else]:
#     <body else> # сработает если во всех выше стоящих условиях пришло False


# string = input('Enter smt: ').lower()

# print(string)
# if string == 'hello':
#     print('Hello, It\'s me, I was wondering if after all these years you\'d like to meet!')
# elif string == 'john':
#     print('Welcome back John Snow! The King of North!')
# elif string == 'abra-kadabra':
#     print('Sim salamon kadabra!')
# else:
#     print('No match found!')
# print('Registration Form:')
# email = input('Enter your email: ')
# if '@' not in email:
#     raise ValueError('Email is Invalid! @ - must be!')

# password = input('Enter the password: ')
# if len(password) < 8:
#     raise ValueError('Too short! At least 8 symbols!')
# elif password.isdigit():
#     raise ValueError('Invalid Password! Only digits!')
# elif password.isalpha():
#     raise ValueError('Invalid Password! Only alphabet!')

# password2 = input('Enter password confirmation: ')

# if password != password2:
#     raise ValueError('Passwords didn\'t match!')

# index = email.find('@')
# print(f'Successfully registered! Hello Mr/Mrs {email[:index]}!')

# age = input('Enter your age: ')

# if age.isdigit():
#     age = int(age)
# else:
#     raise Exception('Invalid value for age!')

# if age < 18:
#     print(f'Access Denied! Come again after {18 - age} year!')
# else:
#     print('You can buy it!')


# Логические операторы
# and - логическое и
# or - лог или
# not - лог отрицание

# money = 1_000
# status = 'base'

# if money > 1_000_000 and status == 'premium':
#     print('You\'re president of our club!')
# elif money > 1_000_000 or status == 'premium':
#     print('You\'re minister of our club!')
# else:
#     print('You\'re honorable member of our club!')



