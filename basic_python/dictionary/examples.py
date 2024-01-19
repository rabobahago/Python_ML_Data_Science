obj = {"name": 'rabo', "age": 24}
print(obj["name"])
alien_x = {"color": 'blue', "size":5}
alien_x['x_color'] = 'green'
alien_x['y_color'] = 'yellow'
print(obj)
print(alien_x)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
   x_increment = 1
elif alien_0['speed'] == 'medium':
   x_increment = 2
else:
# This must be a fast alien.
   x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
fa = favorite_languages['sarah']
print(f'Hello, {fa}')
print(favorite_languages.get('JavaScript', 'JavaScript not in the list'))
for nam in  favorite_languages.keys():
    print(f'{nam}')

for nam in  sorted(favorite_languages.values()):
    print(f'{nam}')


aliens = []
# Make 30 green aliens.
for alien_number in range(30):
   new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
   aliens.append(new_alien)

print('start......')
print(aliens)
print('end......')
# Show the first 5 aliens.
for alien in aliens[:5]:
   print(alien)
#list in a dictionary
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}
cop = pizza.copy()
for topp in pizza['toppings']:
   #print(topp)
   if topp == 'mushrooms':
      print('hello')
print(pizza)

print('cop', cop)

users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
},
}
for username, user_info in users.items():
   print(f"\nUsername: {username}")
   full_name = f"{user_info['first']} {user_info['last']}"
   location = user_info['location']
   print(f"\tFull name: {full_name.title()}")
   print(f"\tLocation: {location.title()}")