
def main():
    print_column(3)
    print_row(4)

def print_column(height):
    for _ in range(height):
        print('#\n', end='')

def print_row(width):
    print('?' * width)

main()
print('.......')
def brick():
    print_sqaure(3)

def print_sqaure(size):
    for i in range(size):
        print(i)
        for j in range(size):
            print('#', end='')
    print()

brick()