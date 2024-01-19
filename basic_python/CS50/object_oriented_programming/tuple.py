def main():
    student = get_student()
    if student[0] == 'Padaw':
        student[1] = 'Raw'
    print(f'{student[0]} from {student[1]}')

def get_student():
    name = input('What is your name: ')
    house = input('What is your house: ')
    return [name, house]

if __name__ == '__main__':
    main()