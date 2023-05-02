#Lists: ordered, mutable, allows duplicate elements
my_list = ['banana', 'orange', 'cherry']
print(my_list)

my_empty = list()
print(my_list)
print(my_list[0])
print(my_list[1])
print(my_list[-1])
print(my_list[-2])
print('........')
#iterate through the list
for x in my_list:
    print(x)
#check if item is in  the list
if 'banana' in my_list:
    print('yes')
else:
    print('no')
#No of element in the list
print(len(my_list))
#append element from the beginning of the list
my_list.append('mango')
my_list.append('lemon')
print(my_list)
#remove element from the list end
my_list.pop()
#reverse a list
print(my_list.reverse())
#remove element that exist in the list
my_list.remove('mango')
my_list.remove('orange')
print(my_list)
#remove all elements from the list
print(my_list.clear())
#sort a list in place
mynum = [8, 7, 1, 3, 6]
mynum.sort()
print(mynum)
#sort list not in place
another = [3, 4, 12, 4, 56]

sort_list_not_place = sorted(another)
print(sort_list_not_place)
print(another)
#multiple list number
multiple = [90] * 8
print(multiple)
#concate list with plus sign
concat_list = multiple + [9]
print(concat_list)
#slicing a list
my_slice_list = [3, 7, 8, 99, 89, 90]
part_slice = my_slice_list[0:1]
print(part_slice)
slice_from_zero = my_slice_list[:4]
print(slice_from_zero)
slice_to_end = my_slice_list[2:]
print(slice_to_end)
slice_from_start_to_end = my_slice_list[:]
print(slice_from_start_to_end)
#step indice
step_one = my_slice_list[::1]
step_two = my_slice_list[::2]
step_reverse = my_slice_list[::-1]
print(step_one)
print(step_two)
print(step_reverse)
#copy original list
original_list = [9, 0, 8, 89, 56]
copy_list = original_list.copy()
copy_list.append(60)
print(copy_list)
print(original_list)
another_copy = list(original_list)
print(another_copy)

#list comprehension
my_list_com = [2, 3, 5, 6, 7, 8,]
comprehen = [i * i for i in my_list_com]
print(my_list_com)
print(comprehen)
i = [2, 4, 6, 30]
print('hello')
gee = [i for el in i if el <= 20]
print(gee)
