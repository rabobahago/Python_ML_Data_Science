# Products
# To find the product of the elements in an array, use the prod() function.
import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([2, 3, 4, 5])
print(np.product(arr1))
print(np.product([arr1, arr2]))
print(np.product([arr1, arr2], axis=1))

# Cummulative Product
# Cummulative product means taking the product partially.
# E.g. The partial product of [1, 2, 3, 4] is [1, 1*2, 1*2*3, 1*2*3*4] = [1, 2, 6, 24]
# Perfom partial sum with the cumprod() function.
# Take cummulative product of all elements for following array:

import numpy as np

arr = np.array([5, 6, 7, 8])
newarr = np.cumprod(arr)
print(newarr)
