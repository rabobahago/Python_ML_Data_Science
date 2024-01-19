#input(*objects, sep=' ', end='\n')
name = input('What is your name: ')
#remove white space from string and capitalize user's name
name = name.strip().title()
print('My name is',name)
#if you want to add extra space from you code
print('My name is ' + name)

#we can change the default parameter
print('My name is ', name, sep='', end='\n')
print('My name is ', name, sep='//', end='\n')
print(f'My name is {name}')