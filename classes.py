#classes:
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