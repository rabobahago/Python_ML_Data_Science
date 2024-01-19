#Person: Use a dictionary to store information about a person you know.
#Store their first name, last name, age, and the city in which they live. You
#should have keys such as first_name, last_name, age, and city. Print each
#piece of information stored in your dictionary.
person = {'first_name': 'Musty', 'last_name': 'Moses', "age": 36, "city": 'Gidan Waya'}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.
names = {'musty': 23, "martins":45, "Tea": 23 }
for key, value in names.items():
    if key == 'musty':
        print(f'Hello {key} you are {names[key]} years old')
    elif key == 'martins':
        print(f'Hello {key} you are {names[key]} years old')
    else:
        print(f'Hello {key} you are {names[key]} years old')

#Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# •	 Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# •	 Use a loop to print the name of each river included in the dictionary.
# •	 Use a loop to print the name of each country included in the dictionary.
rivers = {'nile': 'egypt', 'niger': 'nigeria', 'ele': 'yea'}
for name in rivers:
    print(name)
for name in rivers.values():
    print(name)
ool = {'tea', 'nile', 'niger', 'tea'}


# People: Start with the program you wrote for Exercise 6-1 (page 99).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.
people = {
    "name": {'rabo': 'yusuf', 'rober': 'week'},
    'age':{'rabo': 45, "rober": 40}
}
for key, value in people.items():
    if value['rabo'] == 'rabo':
        val  = value['rabo']
        print(f'Hello {val}')
    elif value['rober'] == 'week':
        val = value['rober']
        print(f'Hello {val}')
    else:
        print(f'Hello there')

# Pets: Make several dictionaries, where each dictionary represents a different pet.
# In each dictionary, include the kind of animal and the owner’s name.
# Store these dictionaries in a list called pets. Next, loop through your list and as
# you do, print everything you know about each pet.
pets = [
    {'name': 'marrot', 'age': 40, 'owner': 'rabo'},
    {'name': 'parro', 'age': 56, 'owner': 'abdul'}
]
for key in pets:
   for n, val in key.items():
     print(key[n])

# Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the information you have stored about it.

state = {
    'kaduna':{"name":'Kaduna', 'country': 'nigeria', 'population': 40000000},
    "lagos":{"name":"lagos", 'country': 'usa', 'population': 30000000},
    "kano":{"name":"kano", 'country': 'usa', 'population': 600000000},
}
for key, value in state.items():
    print(f'"country:" {value["country"]} \n "name:" {value["name"]} \n "population:" {value["population"]}')