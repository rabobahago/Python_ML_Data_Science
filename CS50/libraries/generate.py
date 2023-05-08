import random

coin = random.choice(['heads','tails'])
print(coin)
num = random.randint(1,10)
print(num)

cards = ['King', 'Queen', 'Jack']
random.shuffle(cards)
for card in cards:
    print(card)