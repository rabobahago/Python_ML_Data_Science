# Summations
# What is the difference between summation and addition?
# Addition is done between two arguments whereas summation happens over n elements.
import numpy as np
arr1 = [1, 2, 3]
arr2 = [1, 2, 3]
sum = np.add(arr1, arr2)
sum_ad = np.sum([arr1, arr2])
sum_axis = np.sum([arr1, arr2], axis=1)
print(sum)
print(sum_ad)
print(sum_axis)

# Cummulative Sum
# Cummulative sum means partially adding the elements in array.
# E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].
# Perfom partial sum with the cumsum() function.
import numpy as np
arr = np.array([1, 2, 3])
newarr = np.cumsum(arr)
print(newarr)