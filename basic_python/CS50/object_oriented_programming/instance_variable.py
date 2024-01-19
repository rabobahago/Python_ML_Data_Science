
class Student:
    def __init__(self,name, house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f'{student.name} from {student.house}')

def get_student():
    name = input('Your name: ')
    house = input('Your house: ')
    # instantiate (object)
    return Student(name, house)

@property
def name(self):
    return self.name

@name.setter
def name(self, _name):
    self.name = _name

@property
def house(self):
    return self._house

@house.setter
def house(self, house):
    self._house = house

if __name__ == '__main__':
    main()