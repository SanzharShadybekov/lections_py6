# ORM (Object-Relational Mapping) - технология программирования, благодаря которой разработчики могуть использовать язык программирования для взаимодействия с реляционной базой данных(PostgreSQL, MySQL и тд). Вместо того чтобы писать сырые запросы(опареторы SQL), вы будете писать код на языке прог. Это очень сильно ускоряет разработку приложения и бд, особенно на начальных этапах.


from peewee import PostgresqlDatabase


db = PostgresqlDatabase(
    database='orm_db',
    user='sanzhar',
    password='1',
    host='localhost', # 127.0.0.1
    port=5432    
)

# a = db.connect()
# print(a)


