#Dictionary: Key-Value pairs, Unordered, mutable
my_dict = {'name': 'Rabo', 'value': 40}
print(my_dict)
another_dict = dict(age = 40, name = 'Rabo',)
print(another_dict)
#accessing element from a dictionary
print(my_dict['name'])
print(another_dict['name'])
#adding element to a dictionary
my_dict['address'] = 'hello my address'
print(my_dict)
#check to see if something is in the dictionary
if 'name' in my_dict:
    print(my_dict['name'])

#try and catch
try:
    print(my_dict['name'])
except:
    print('Error')
#delete item
del my_dict['name']
print(my_dict)
my_dict.pop('address')
print(my_dict)
my_dict.popitem()
print(my_dict)
#loop through the dictionary
my_dict_u = {"name":'Rabo', "age": 55}
for key in my_dict_u.keys():
    print(key)
for value in my_dict_u.values():
    print(value)
for key, val in my_dict_u.items():
    print(key, val)
#copy dictionary
dictionaries = {"address": 'No 80 street tue', 'age': 55}
copy_dict = dict(dictionaries)
copy_ex = dictionaries.copy()
copy_ex['tea'] = 600
copy_dict['color'] = 'red'
print(dictionaries)
print(copy_dict)
print(copy_ex)

name_dict = {'name': 'Yusuf'}
age_dict = {'age': 60}
house_dict = {'num': 6}
name_dict.update(age_dict)
name_dict.update(house_dict)
print(name_dict)
# we can use tuple and number as keys in the dictionary