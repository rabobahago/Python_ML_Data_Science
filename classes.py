# classes:
class MyClass:
    x = 800


prop = MyClass()
print(prop.x)


class Person:
    def __init__(self, age, name):
        self.name = name
        self.age = age

    def __str__(self):
        return f'My name is {self.name} and I am {self.age} years old.'


person = Person(40, 'Rabo')
print(person)


class Person:
    def __init__(self, name, age, action):
        self.name = name
        self.age = age
        self.action = action

    def __str__(self):
        return f'My name is {self.name} and I am {self.age} years old.'

    def printAction(self):
        print(self.action)


person = Person('Rabo Yusuf', 30, 'I Love human being naturally')
print(person.printAction())


class Circle:
    def __init__(self, radius, center) -> None:
        '''Initalize the center's center and radius'''
        # radius most be a positive number
        if radius < 0:
            raise ValueError('Radius can\'t be negative')
        self.radius = radius
        self.center = center

    def get_radius(self):
        '''Return the radius of the class'''
        return self.radius

    def get_center(self):
        '''Return the radius of the class'''
        return self.center

    def get_area(self):
        '''It return the area of circle'''
        from math import pi
        return pi * self.radius ** 2

    def get_circumference(self):
        '''return the circumference of a circle'''
        from math import pi
        return 2 * pi * self.radius

    def move_center(self, pt):
        '''Move the center to pt'''
        self.center = pt

    def grow(self):
        '''expand the radius by 1'''
        self.radius += 1

    def shrink(self):
        '''decrease the radius by one'''
        if self.radius > 0:
            self.radius -= 1
