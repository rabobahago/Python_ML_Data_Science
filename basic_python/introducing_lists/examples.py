#list

bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles[0])
print(bicycles[1])

#adding element from a list
bicycles[0] = 'cycle'
print(bicycles)
bicycles.insert(2, 'motorcycle')
print(bicycles)
bicycles.append('lorry')
print(bicycles)
another = bicycles.copy()
print('hey:', another)

#removing element from a list
del bicycles[0]
print(bicycles)
print(bicycles.pop())
print(bicycles)
print(bicycles.pop(1))
print(bicycles)

#remove item by value
fruits = ['orange', 'mango', 'cashew']
print(fruits)
print(fruits.remove('orange'))
print(fruits)
#sort item
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

print(len(cars))

list_names = ['car', 'motorcycle', 'main']
print(list_names)
print(len(list_names))
