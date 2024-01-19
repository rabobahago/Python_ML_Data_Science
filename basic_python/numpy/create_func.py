import numpy as np

def add(x, y):
    return x + y
def mul(x, y, z):
    return x * y + z
sum = np.frompyfunc(add, 2, 1)
multiple = np.frompyfunc(mul, 3, 1)
print(sum([1, 2, 3, 4], [3, 4, 5, 6]))
print(multiple([1, 2, 3, 4], [3, 4, 5, 6], [3, 4, 5, 6]))