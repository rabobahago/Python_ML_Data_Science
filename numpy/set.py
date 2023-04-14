# What is a Set
# A set in mathematics is a collection of unique elements.
# Sets are used for operations involving frequent intersection, union and difference operations.
# Create Sets in NumPy
# We can use NumPy's unique() method to find unique elements from any array.
# E.g. create a set array, but remember that the set arrays should only be 1-D arrays.

#Convert following array with repeated elements to a set:

import numpy as np
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)
print(x)

# Find union of the following two set arrays:
import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.union1d(arr1, arr2)
print(newarr)

#Find intersection of the following two set arrays:

import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.intersect1d(arr1, arr2, assume_unique=True)
print(newarr)

#Find the difference of the set1 from set2:
import numpy as np
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
newarr = np.setdiff1d(set1, set2, assume_unique=True)
print(newarr)

#Find the symmetric difference of the set1 and set2:
import numpy as np
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
newarr = np.setxor1d(set1, set2, assume_unique=True)
print(newarr)