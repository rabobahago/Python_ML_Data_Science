#Finding LCM (Lowest Common Multiple)
# The Lowest Common Multiple is the smallest number that is a common multiple of two numbers.
# Find the LCM of the following two numbers:
import numpy as np
num1 = 4
num2 = 6
x = np.lcm(num1, num2)
print(x)

# Finding LCM in Arrays
# To find the Lowest Common Multiple of all values in an array, you can use the reduce() method.
# The reduce() method will use the ufunc, in this case the lcm() function, on each element, and reduce the array by one dimension.
# Find the LCM of the values of the following array:

import numpy as np
arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr)
print(x)