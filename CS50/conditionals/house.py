name = input('what is your name: ')
if name == 'Harry' or name == 'Hermoine' or name == 'Ron':
    print('Gryffindor')
elif name == 'Draco':
    print('Slytherin')
else:
    print('who')

#Another version
match name:
    case 'Harry' | 'Hermoine' | 'Ron':
        print('Gryffindor')
    case 'Draco':
        print('Slytherin')
    case _:
        print('who')