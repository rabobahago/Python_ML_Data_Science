#Strings: ordered, immutable , text representation
my_string = 'Hello world!'
print(my_string)
#multiple line
my_str = """hello
world"""
print(my_str)
#access character
my_immutable = 'Hello redbull'
print(my_immutable[0])
print(my_immutable[1])
print(my_immutable[-2])
print(my_immutable[-1])
#slicing string
my_slicing = 'Hello redbull'
my_slice = my_slicing[0:]
my_sl = my_slicing[:len(my_slice)]
print(my_sl)
my_step = my_slice[::2]
print(my_step)
for i in my_step:
    print(i)
if 'H' in my_slicing:
    print('yes')
else:
    print('no')

#string with white space
my_space = ' hello world '
my_strip = my_space.strip()
print(my_strip)

#Turn to Upper case or Lower case
my_upper = my_space.upper()
my_lower = my_space.lower()
print(my_upper, my_lower)

#start with
my_start = my_lower.startswith('h')
print(my_start)
my_end = my_lower.endswith('e')
print(my_end)
my_find = my_lower.find('h')
print(my_find)
#count number of characters
print(my_space.count('p'))
#replace
my_space = 'hello, world'
print(my_space.capitalize())
my_replace = my_space.replace('hello', 'Hi')
print(my_replace)
my_list_from = my_space.split(',')
print(my_list_from)
my_list_word = ['hey', 'you', 'are', 'doing', 'well']
strings_from_list = ' '.join(my_list_word)
print(strings_from_list)
#formatting a string old format
var = 'Rabo'
formated = 'Hello %s' % var
print(formated)
#digit
var = 300
num = 'ehh %d' % var
print(num)
variable = 3.566789
num = 'dollar %f' % variable
print(num)

#format method
var = 6.6666
gee = 6.77777
bee = 'the number is {} and {:.2f}'.format(var,gee)
print(bee)
#f-string format
var = F'hey {var * 2}'
print(var)
