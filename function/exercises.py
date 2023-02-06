# Message: Write a function called display_message() that
# prints one sentence telling everyone what you are learning about in this chapter. Call the
# function, and make sure the message displays correctly.
def message():
    print('I am leaning Python')
message()

# Favorite Book: Write a function called favorite_book() that accepts one
# parameter, title. The function should print a message, such as One of my
# favorite books is Alice in Wonderland. Call the function, making sure to
# include a book title as an argument in the function call.
def favorite_book(title):
    print(f'I love {title}')
title = input('What is your favorite book: ')
favorite_book(title)

# Cities: Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the
# default country.
def describe_city(city='Kaf', country='Nigeria'):
    print(f'{city} {country}')
describe_city()
describe_city('Lagos', 'Nigeria')


# Sending Messages: Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed. After
# calling the function, print both of your lists to make sure the messages were
# moved correctly.
def copy_messages(messages, copy_message):
    while messages:
        mess = messages.pop()
        copy_message.append(mess)
def send_messages(copy_message):
    for message in copy_message:
        print(message)
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
copy_messages(unprinted_designs, completed_models)
send_messages(completed_models)