# Rental Car: Write a program that asks the user what kind of rental car they
# would like. Print a message about that car, such as “Let me see if I can find you
# a Subaru.”
message = input("What kind of rental car do you want? ")
print(f'Let me see if I can find you {message}')

# Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a
# message saying they’ll have to wait for a table. Otherwise, report that their table is ready.
num = input("How many people are in your dinner group? ")
num_people = int(num)
if num_people > 8:
    print(f'they’ll have to wait for a table')
else:
    print(f'report that their table is ready')