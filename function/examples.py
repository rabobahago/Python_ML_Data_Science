from typing import Any, Callable


def get_name():
    print('hello world')


get_name()


def get_age(age):
    print(f'Hello {age}')


inp = input('Enter age: ')
get_age(inp)


def get_gender(gende):
    return gende.title()


gen = get_gender('hello')
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
first, *second = [90, 45, 67]
print(first)
print(second)
nums = [90, 45, *second]
print(nums)


def get_ages(*args: int) -> None:
    for age in args:
        print(age)


get_ages(20, 34, 45, 68, 89)


def get_detail(**kwargs: Any) -> None:
    for key, val in kwargs.items():
        print(f'The key {key} has a value of {val}')


get_detail(name='Badman', age=34, life=230)
get_detail(name='Superman', age=50, life=500)


def invoice(product: str, *args: str, **kwargs) -> None:
    print(product)
    print(args)
    print(kwargs)


invoice('Sneakers', 'black', 'white', brand='Nike',
        category='Air Jordans', prices=899.99, in_stock=False)


def greet_rabo(name: str) -> None:
    print(f'Hello {name}')


def good_morning(name: str) -> None:
    print(f'Good Morning {name}')


def good_evening(name: str) -> None:
    print(f'Good evening {name}')


def universal(name: str, fn: Callable[[str], None]):
    val = fn(name)
    print(val)


universal('Rabo', greet_rabo)
universal('Withdren', good_evening)


def get_num() -> Callable[[int], int]:
    def supply_num(num: int) -> int:
        return num + 5
    return supply_num


val = get_num()
print(val(6))
