#itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby
import operator
a = [2, 3]
b = [4, 5]
prod = list(product(a, b))
print(prod)
c = [1, 2]
d = [1, 2, 3]
perm = list(permutations(c))
print(perm)
per = list(permutations(d))
print(per)
com = list(combinations(c,2))
print(com)
com_with = list(combinations_with_replacement(d,2))
print(com_with)
sum = list(accumulate(d))
print(sum)
mul_self = list(accumulate(c, func=operator.mul))
print(mul_self)

def less_than(x):
    return x < 3
group_object = groupby(d, key=lambda x: x < 3)
for key, value in group_object:
    print(key, list(value))
list_dict = [{"name": "rabo", "age":4}, {"name": "rabo", "age":33}, {"name": "yusuf", "age":4}]
group_object = groupby(list_dict, key=lambda x: x['age'])
for key, value in group_object:
    print(key, list(value))