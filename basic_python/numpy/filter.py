# Filtering Arrays
# Getting some elements out of an existing array and creating a new array out of them is called filtering.
# In NumPy, you filter an array using a boolean index list.
# A boolean index list is a list of booleans corresponding to indexes in the array.
# If the value at an index is True that element is contained in the filtered array, if the value
# at that index is False that element is excluded from the filtered array.
# Create an array from the elements on index 0 and 2:

import numpy as np
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]

print(newarr)

# Creating the Filter Array
# In the example above we hard-coded the True and False values,
# but the common use is to create a filter array based on conditions.
# Create a filter array that will return only values higher than 42:

import numpy as np

arr = np.array([41, 42, 43, 44])
print(arr)
filter_arr = []
for element in arr:
    if element > 41:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
x =arr[filter_arr]
print(x)

#Create a filter array that will return only even elements from the original array:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)