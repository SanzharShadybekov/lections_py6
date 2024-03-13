from views import CreateMixin, ReadMixin, UpdateMixin, DeleteMixin


class SmartPhones(CreateMixin, ReadMixin, UpdateMixin, DeleteMixin):
    pass

smartphones = SmartPhones()
print(smartphones.post(title='Redmi Note 10', description='The best phone for own price!', qty=10, price=250))
print(smartphones.post(title='Redmi Note 20', description='Flagman of redmi phones', qty=5, price=500))
print(smartphones.post(title='Iphone 14 Pro Max', description='New cool and super phone!', qty=5, price=1300))
print(smartphones.post(title='Samsung S22 Ultra', description='The best phone for adnroid lovers!', qty=3, price=1000))
print(smartphones.post(title='Iphone 13 Pro Max', description='Classic phone for iphone users!', qty=15, price=1000))
print()
print()
print(smartphones.list())
print()
print(smartphones.detail(3))
print()
print(smartphones.detail(12))
print(smartphones.detail(0))
print(smartphones.detail(1))
print()
print(smartphones.patch(1, title='Redmi Note 30'))
print()
print(smartphones.detail(1))
print()
print(smartphones.delete(12))
print(smartphones.delete(1))
print()
print()
print(smartphones.list())
