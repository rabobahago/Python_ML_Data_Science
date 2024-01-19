name = ['White', 'Brown', 'Green']
def get_color(first, second, third, fourth='Yellow'):
    print(f'My favorite colors are {first} | {second} | {third} | {third} | {fourth}')

get_color(*name)

def total(galleons, sickles, knut):
    return (galleons * 17 + sickles) * 29 + knut
coin = {"galleons": 100, 'sickles': 50, 'knut': 50}
print(total(**coin), 'Knuts')


def f(*args, **kwargs):
    print(f'Positional: {args}, named: {kwargs}')

f(20, 30, 50, dog=34, cats='40')