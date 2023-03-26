#Set: unordered, mutable and no dublicate
my_set = {3, 4, 5, 6, 3}
print(my_set)
str_set = set('hello')
print(str_set)
#create and empty set
empty_set = set()
print(empty_set)
my_set.add(30)
my_set.add(60)
my_set.remove(30)
my_set.discard(30)
print(my_set)
#loop over a set
for i in my_set:
    print(i)
#check to see if element is in the set
if 7 in set(my_set):
    print('Ys')
#union and interception
odds = {1, 3, 5, 7}
evens = {0, 2, 4, 6}
primes = {2, 3, 5, 7}
uni = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
u = odds.union(evens)
print(u)
i = odds.intersection(evens)
print(i)
diff = odds.difference(primes)
print(diff)
sym_diff = odds.difference(primes)
print(sym_diff)
print(uni.issubset(primes))
print(primes.issubset(uni))
uniCopy = uni.copy()
uniCopy.add(800)
print(uniCopy)