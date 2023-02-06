def get_name():
    print('hello world')
get_name()

def get_age(age):
    print(f'Hello {age}')
inp = input('Enter age: ')
get_age(inp)

def get_gender(gende):
    return gende.title()

gen= get_gender('hello')
print(gen)
def get_num_of_player(*age):
    for ag in age:
        print(f'Age: {ag}')
get_num_of_player(3, 5, 5)
def get_num_of(name, *age):
    print(f'Name: {name}')
    for ag in age:
        print(f'Age: {ag}')
get_num_of('rabo', 7, 8, 9)
