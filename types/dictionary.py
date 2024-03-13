# dict() - Словарь -> упорядоченная коллекция элементов(python 3.7 -> ordered). Каждый элемент внутри словаря хранится в виде пары --> {ключ: значение}

# ассоциативный массив, hash table, object(js), structure == dictionary(py)

# ключами могуть только неизменяемые типы данных и в словаре сохраняются только уникальные ключи
# тогда как значениями могут выступать любые типы данных и любые значения

# thisdict = {
#     'brand': 'Ford',
#     'year': 1967,
#     'model': 'Mustang',
# }
# ls = ['Ford', 1967, 'Mustang']

# print(thisdict, type(thisdict))
# print(thisdict['brand'], thisdict['model'])
# print(thisdict['year'])

# thisdict['motor'] = 'GTI Turbo'
# thisdict['model'] = 'fiesta'
# print(thisdict)

# -------------------------
# print(dir(dict))
# items, keys, values

user_info = {
    'first_name': 'John', 
    'last_name': 'Snow',
    'age': 24,
    'email': 'bastard123@gmail.com',
    'role': 'admin',
}
# print(user_info)

# ls = list(user_info.keys())
# print(ls)

# ls2 = list(user_info.values())
# print(ls2)

# ls3 = list(user_info.items())
# print(ls3)
# print('\nValues:')
# for value in user_info.values():
#     print(value)

# print('\nKeys:')
# for key in user_info.keys():
#     print(key)

# print('\nItems:')
# for key, value in user_info.items():
#     print(f'keys: {key}, values: {value}') 

# изменение
# dict_ = {'name': 'Jack', 'age': 17}
# print(dict_)
# dict_['name'] = 'John'
# dict_['address'] = 'WinterFell'
# print(dict_)
# dict_.update(age=24, address='BlackCastle')
# print(dict_)
# dict_.update({'name': 'John Snow'})
# print(dict_)
# ----------------------
# dict_ = {1: 'Pizza', 2: 'Burger', 3: 'Steak'}
# print(dict_[3], '!!!')
# print(dict_.get(5))

# setdefault - работает так же как get, но если нет такого ключа то создает новую пару из этого ключа

# dict_ = {1: 'Pizza', 2: 'Burger', 3: 'Steak'}
# print(dict_.setdefault(5, 'Manty'))
# print(dict_)

# ----------------------------
# создание - fromkeys
# ls = list(range(1, 20))
# new_dict = dict.fromkeys(ls, 'default')
# print(new_dict)

# -------------------
# удаление элементов
# pop, popitem

# pop(<key>) - удаляет пару по ключу
# popitem() - удаляет последнию пару

# dict_ = {'name': 'Jonh', 'last_name': 'Snow', 'age': 24}
# print(dict_)
# removed = dict_.pop('last_name')
# print(dict_)
# print(removed)
# print('------------------------')
# removed = dict_.popitem()
# print(dict_)
# print(removed)

# ----------------------------------------
roles = {
    1: 'Admin',
    2: 'Customer',
    3: 'Vendor',
}
users = {
    55: {
        'id': 55, 'role': roles[3], 'username': 'Tirion',
    },
    12: {
        'id': 12, 'role': roles[1], 'username': 'John Snow',
    },
    4: {
        'id': 4, 'role': roles[2], 'username': 'Raychel'
    }
}
print(users)

product = {
    'id': 1,
    'title': 'Samsung Galaxy S23 Ultra',
    'description': 'lorem ipsum',
    'price': 1000
}
print(product)

id_user = int(input('Vvedite id: ')) # 12
if users[id_user]['role'] == roles[1]:
    product['description'] = input('Vvedite opisaniye: ')
else:
    print('You don\'t have permissions!')
    
print()
print(product)