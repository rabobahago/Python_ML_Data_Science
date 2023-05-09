students = []
with open('students.csv') as file:
    for lines in file:
        name, house = lines.rstrip().split(',')
        student = {'name': name, 'house': house}
        students.append(student)
def get_name(student):
    return student["name"]
for student in sorted(students, key=get_name):
    print(f"{student['name']} is in house {student['house']}")
