x = int(input('what is x: '))
if x % 2 == 0:
    print('Even...')
else:
    print('Odd')

print('.........')

def main(x):
    print('Even') if is_even(x) else print('Odd')
    # if is_even(x):
    #     print('Even')
    # else:
    #     print('Odd')

def is_even(n):
    return n % 2 == 0
    # return True if n % 2 == 0 else False
main(x)