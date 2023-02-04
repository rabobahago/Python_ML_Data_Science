#conditional statement
names = ['Rabo', 'Kenneth', 'John', 'Juan', 'Yahu']
for name in names:
    if name == 'Rabo':
        print(name.upper())
    else:
        print(name.title())

print('hello world' == 'hello world')
print('world' == 'world' and 3 == 3)
print(3 > 1 or 3 == 3)
print('world' == 3)

print("rabo".title() in names)

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
