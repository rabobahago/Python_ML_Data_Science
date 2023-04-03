#boolean
print(3 > 7)
print(6 > 2)
#basic boolean
x, y = False, True
r = x and y
print(r) #False
e = x or y
print(e) #True
d = not y
print(d)

#while loop with break
n = 0
while(True):
    n += 1
    print(n)
    if(n == 10):
        break

#class
class Beer:
    def __init__(self):
        self.content = 1.0
        self.items = []
        self.length  = 0
    def drink(self):
        self.content = 400
        return self.content
    def add(self, item):
        self.length += 1
        self.items.append(item)
        return self.length
    def get_items(self):
        return self.items
beer = Beer()
print(beer.drink())
beer.add(3)
beer.add(5)
print(beer.get_items())

#if elif else
n = 20
if n == 20:
    print('within the bound')
elif n < 5:
    print('out of the bound')
else:
    print('hi else')
#for loop
for i in [2, 4, 5, 6]:
    print(i)
#while loop
i = 1
while(i < 20):
    print(i)
    i += 1
#check to see if both element point to the same object
x = y = 40
print(x is y)
print([3] is [3])
print((3) is (3))
print({"name" : "rabo"} is {"name" : "rabo"})

#input number
number = int(input("please a number: "))
if(number < 20):
    print('small number')
else:
    print('medium number')

#lamba
lam = lambda x: x + 200
print(lam(4))

#boolean
x, y = True, False
print(not x and y or not x and y)
if 5:
    print("false")
else:
    print("true")
y, x = 3, 2
print(y - x)
print(y + x)
print(y * x)
print(y / x)
print(y // x)
print(y % x)
print(-x)
print(abs(-x))
print(int(9.96))
print(float(9))
print(y**x)
#string
s = 'The youngest pope was 11 years old'
print(s[0])
print(s[1:3])
print(s[-3:-1])
print(s[-3:])
x = s.split()
print(x[-3] + ' ' + x[-2] + ' ' + x[-1] + ' ' + x[-5])
y = ' This is lazy\t\n '
print(y.strip())
print('DrDre'.lower())
print('attention'.upper())
print('smartphone'.startswith('smart'))
print('smartphone'.endswith('phone'))
print('another'.find('other'))
print('cheat'.replace('ch', 'n'))
print(','.join(['R', 'E', 'A', 'D']))
print('ear' in 'earth')
print(len('helllllllllll'))
l = [2, 34, 5]
print(len(l))
print(l.append(8))
print(l.insert(2, 100))
print(l + [5])
r = [30, 5, 7]
print(r.index(7, 1))
print(r.reverse())
print(r)
print(r.sort())
print(r)
#stack
a = [3]
a.append(30)
a.pop()
a.pop()
print(a)
#set
basket = {'carrot', 'mango'}
name = set(['rabo', 'yusuf'])
#dictionary
fruit = {"carrot": 80, "apple": 700}
print(fruit['apple'] < fruit['carrot'])
print(fruit['carrot'] < fruit['apple'])
print('apple' in fruit.keys())
print(50 < list(fruit.values())[0])
food = {'apple', 'egg', 'banana', 'orange'}
print('mushroom' in food)
print('apple' in food)
for x in range(5):
    print(x)
print(x * 30 for x in [4, 6] if x < 2 )
#map
print(list(map(lambda x: x[0]  + 'ee', ['hello', 'world'])))
print(list(filter(lambda x: True if x < 45 else False, [3, 6, 90, 5,7, 34])))
print(list(map(lambda x, y, z: str(x) + ' ' + y + ' ' + str(z), [20, 30, 123], ['week', 'tee', 'weak'], [90, 34, 112])))
print(' mar '.join(list(['rabo', 'yusuf'])))
str = 'hello world'
print(help(str))
#unpack argument
print(list(zip(['read', 'write'], [2, 40])))
def f(x, y, z): return x + y * z
print(f(*[1, 2, 3]))
print(f(**{'x':1, 'y': 2, 'z': 40}))
x, *y = [2, 4, 6, 8]
print(x)
x = {"name": "rabo"}
y = {'age': 45}
p = {**x, **y}
print(p)
