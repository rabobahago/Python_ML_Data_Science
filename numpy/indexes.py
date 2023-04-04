import numpy as np
arr = np.array([1, 2, 3])
print(arr[0])
print(arr[1] + arr[2])
arr = np.array([[1, 2, 3], [7, 8, 10]])
print('2nd element on 2nd row: ', arr[1, 1])
# Access 2-D Arrays
# To access elements from 2-D arrays we can use comma
# separated integers representing the dimension and the index of the element.

# Think of 2-D arrays like a table with rows and columns, where the
# dimension represents the row and the index represents the column.
# Access 3-D Arrays
# To access elements from 3-D arrays we can use comma separated integers representing the dimensions and the index of the element.
# Access the third element of the second array of the first array:


arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])

# Negative Indexing
# Use negative indexing to access an array from the end.
# Print the last element from the 2nd dim:

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])
