def main():
    n = get_number()
    return print_meow(n)

def get_number():
    while True:
        n = int(input('what is n: '))
        if n > 1:
            return n
def print_meow(n):
    for _ in range(n):
        print("meow")
main()