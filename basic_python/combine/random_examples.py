import random, secrets
a = random.random()
print(a)
b = random.randint(1, 10)
print(b)
c = random.randrange(1, 10)
print(c)
d = random.normalvariate(0, 2)
print(d)
list_char = list('ABCDEFGH')
random_choice = random.choice(list_char)
print(random_choice)

random_more = random.sample(list_char, 3)
print(random_more)

random_shuffle = random.shuffle(list_char)
print(random_shuffle)

a = secrets.randbits(4)
print(a)