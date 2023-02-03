#Store the names of a few of your friends in a list called names. Print
#each person’s name by accessing each element in the list, one at a time.
names = ['Rabo', 'Faruck', 'Barry']
print(names[0])
print(names[1])
print(names[2])
#print(names[3])

#Greetings: Start with the list you used in Exercise 3-1, but instead of just
#printing each person’s name, print a message to them. The text of each message
#should be the same, but each message should be personalized with the
#person’s name.
for name in names:
    print(f'Hello, {name}! Love you all')

#Your Own List: Think of your favorite mode of transportation, such as a
#motorcycle or a car, and make a list that stores several examples. Use your list
#to print a series of statements about these items, such as “I would like to own a
#Honda motorcycle.”
mode_of_transportation = ['Road', 'Motorcycle', 'bikecycle'];
for transport in mode_of_transportation:
    print(f'I would like to own a {transport}')

#Guest List: If you could invite anyone, living or deceased, to dinner, who
#would you invite? Make a list that includes at least three people you’d like to
#invite to dinner. Then use your list to print a message to each person, inviting
#them to dinner
invite = ['Rabo', 'Yusuf', 'Kenneth']
for name in invite:
    print(f'Hi {name}, you are invited to to my dinner party tomorrow')

#Changing Guest List: You just heard that one of your guests can’t make the
#dinner, so you need to send out a new set of invitations. You’ll have to think of
#someone else to invite.
#•	 Start with your program from Exercise 3-4. Add a print() call at the end
#of your program stating the name of the guest who can’t make it.
#•	 Modify your list, replacing the name of the guest who can’t make it with
#the name of the new person you are inviting.
#•	 Print a second set of invitation messages, one for each person who is still
#in your list.
name_remove = invite[1]
replaceInviteNames = invite.insert(1, 'Martins')
for name in invite:
    print(f'Hello, {name}. I am sending you a reminder')
print(f"Hi everyone, Guest by the name {name_remove} can't make it")

#Store the locations in a list. Make sure the list is not in alphabetical order.
#Use sorted() to print your list in alphabetical order without modifying the
#actual list.
# Show that your list is still in its original order by printing it.
#Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
#Show that your list is still in its original order by printing it again.
animal = ['goat', 'hen', 'cock', 'cat', 'horse', 'dog', 'bee']
print(sorted(animal))
print(animal)
print(sorted(animal, reverse=True))
print(animal)
#Use reverse() to change the order of your list. Print the list to show that its
#order has changed.
#Use reverse() to change the order of your list again. Print the list to show
#it’s back to its original order.
animal.reverse()
print(animal)
animal.reverse()
print(animal)

#Use sort() to change your list so it’s stored in alphabetical order. Print the
#list to show that its order has been changed.
#Use sort() to change your list so it’s stored in reverse alphabetical order.
#Print the list to show that its order has changed
animal.sort()
print(animal)
animal.sort(reverse =True)
print(animal)
#Working with one of the programs from Exercises 3-4
#through 3-7 (page 42), use len() to print a message indicating the number
#of people you are inviting to dinner
print(len(animal))
print(animal[-1])