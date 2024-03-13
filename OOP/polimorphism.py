# функция полиморфизм -> len(): __len__
# print(len('Makers'))
# print(len([1,2,3,4,5]))
# print(len({1: 2, 3: 4, 5: 6}))

# + (__add___) - метод
# print(5 + 5)
# print('hello ' + 'world')
# print([1,2,3] + [4,5,6])


# Полиморфизм - способность функции(метода) использоваться для разных типов(классов)
# Широко распрастраненное опрделение: "один интерфейс - много реализаций"
# list.pop
# set.pop
# dict.pop

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age 

#     def info(self):
#         print(f'It\'s a cat. Cats name is {self.name}, age: {self.age}') 
    
#     def make_sound(self):
#         print('meow, meow!')


# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age 

#     def info(self):
#         print(f'It\'s a dog. Dogs name is {self.name}, age: {self.age}') 
    
#     def make_sound(self):
#         print('bark, bark!')

# cat = Cat('Garfild', 5)
# dog = Dog('Pluto', 6)

# for obj in (cat, dog):
#     obj.info()
#     obj.make_sound()

from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name) -> None:
        self.name = name 
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def fact(self):
        pass

class Square(Shape):
    def __init__(self, length) -> None:
        super().__init__('Квадрат')
        self.length = length

    def area(self):
        return self.length ** 2
    
    def fact(self):
        return 'У квадрата все стороны равны и углы равны 90 градусам!'

class Circle(Shape):
    def __init__(self, radius) -> None:
        super().__init__('Окружность')
        self.radius = radius
        
    def area(self):
        from math import pi
        return pi * self.radius ** 2

    def fact(self):
        return 'Окружность- это множество точек плоскости, расстояние которых до данной точки (центра окружности) одинаково.'
    
a = Square(8)
b = Circle(4)

print(a.fact())
print(a.area())

print(b.fact())
print(b.area())