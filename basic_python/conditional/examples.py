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

if 3 > 1:
    print('the left number is small')
elif 3 < 1:
    print('the right number is big')
else:
    print('the left number is moderate')
names = [2]
if names:
    print('list is not empty')
else:
    print('list is empty')

available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for available_toppings in available_toppings:
    if available_toppings in requested_toppings:
        print(f'{available_toppings}')
    else:
        print(f'Not in the list')
