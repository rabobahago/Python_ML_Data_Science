#Think of at least three kinds of your favorite names. Store these
#in a list, and then use a for loop to print the name of each names.
names = ['Audu', 'Keita', 'Kelas', 'tead']
for name in names:
    print(name)

#Modify your for loop to print a sentence using the name of the names
#instead of printing just the name. For each name you should
#have one line of output containing a simple statement like I like pepperoni
#pizza
for name in names:
    print(f'Hi {name}, I am the only person here')
print(f'We have {len(names)} people in this list')

#Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
#inclusive.
for num in range(1,21):
    print(num)

#One Million: Make a list of the numbers from one to one million, and then
#use a for loop to print the numbers. (If the output is taking too long, stop it by
#pressing ctrl-C or by closing the output window.)
for num in range(1, 1001):
    print(num)

#Summing a Million: Make a list of the numbers from one to one million,
#and then use min() and max() to make sure your list actually starts at one and
#ends at one million. Also, use the sum() function to see how quickly Python can
#add a million numbers.
for num in range(1, 100):
    print(num)
print(sum(list(range(1, 1000001))))

#Odd Numbers: Use the third argument of the range() function to make a
#list of the odd numbers from 1 to 20. Use a for loop to print each number
for num in range(0,20, 2):
    print(num)

#Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
#print the numbers in your list.
for num in range(3, 30, 3):
    print(num)
print('cubic')

#Cubes: A number raised to the third power is called a cube. For example,
#the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
#is, the cube of each integer from 1 through 10), and use a for loop to print out
#the value of each cube.
cubic = [value **3 for value in range(1, 11)]
for num in cubic:
    print(num)

#Slices: Using one of the programs you wrote in this chapter, add several
#lines to the end of the program that do the following:
#•	 Print the message The first three items in the list are:. Then use a slice to
#print the first three items from that program’s list.
#•	 Print the message Three items from the middle of the list are:. Use a slice to
#print three items from the middle of the list.
#•	 Print the message The last three items in the list are:. Use a slice to print the
#last three items in the list.
average = [3, 5, 6, 8, 4, 5, 6, 8]
print(f'first three item in the list are: {average[:3]}')
print(f'three item in the list from the middle: {average[len(average) - 6: 4]}')

#tuple
tu = (3, 5, 7, 89)
print(tu[0])

for num in tu:
    print(num)