# import sys
# Turple: ordered, mutable, allows duplicate elements. Can't be change after it creation
# Note also that the parathesis is optional
my_tuple = (23, 24, 25, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 26, 'hi')
print(my_tuple)
my_without_tuple = 2, 4, 6
print(my_without_tuple)
# single element turple must have a trailing comma
single_tuple = (1,)
print(single_tuple)
# create a turple from a list for example
my_list_tuple = tuple([8, 89, 90,])
# access element
print(my_list_tuple)
print(my_list_tuple[0])
print(my_list_tuple[1])
print(my_list_tuple[-1])
print(my_list_tuple[-2])
# iterate element
for i in my_list_tuple:
    print(i)
# check whether element exist in tuple
if 23 in my_list_tuple:
    print('yes')
else:
    print('no')

# number of elements in tuple
print(len(my_list_tuple))
# count repeated element in tuple
print(my_tuple.count(23))
# find the index of a particular
print(my_tuple.index(23))
print(my_tuple.index('hi'))
# convert tuple to a list
list_from_tuple = list(my_tuple)
print(list_from_tuple)

# copy part tuple
copy = my_tuple[:2]
print(copy)
# destructuring
my_names = 'Rabo', 'Yusuf', 'Bahago'
first_name, middle_name, last_name = my_names
print(first_name)
print(middle_name)
print(last_name)
# destructuring between
my_tuple_number = (68, 89, 8, 12, 23, 45, 56)
num, * num2, num3 = my_tuple_number
print(num)
print(num2)
print(num3)
# compare a list and tuple
# my_list_k = (1, 3, 4, 'hello', True)
# my_tuple_k = [1, 3, 4, 'hello', True]
# print(sys.getsizeof(my_list_k), 'bytes')
# print(sys.getsizeof(my_tuple_k), 'bytes')

my_tuple = (2, 3, 4, 5, 6)
print(my_tuple[0])
for elem in my_tuple:
    print(elem)
print(my_tuple[2:4])
my_list1 = [2, 3, 5]
my_list2 = [5, 79,]
print('..............')
for i in zip(my_list1, my_list2):
    print(i)
print(range(10, 15))
my_dict = {'name': 'Rabo', 'age': 67, }
print(isinstance(my_dict.keys(), dict))
my_list = [2, 4, 6, 4, 2, 7]
a = list(dict.fromkeys(my_list).keys())
print(a)
(1, 3, 45) + (90)
