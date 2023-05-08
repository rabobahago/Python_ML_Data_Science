def main():
    x= get_int("what's x? ")
    print(f'x is: {x}')
def get_int(prompt):
    i = 0
    while True:
        try:
            x = int(input(prompt))
            i += 1
            return x
        except ValueError:
            i += 1
            if i == 1:
                print('x is not an integer')
            else:
                pass
main()