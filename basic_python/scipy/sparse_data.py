# What is Sparse Data
# Sparse data is data that has mostly unused elements (elements that don't carry any information ).
# It can be an array like this one:
# [1, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0]
# Sparse Data: is a data set where most of the item values are zero.
# Dense Array: is the opposite of a sparse array: most of the values are not zero.
# In scientific computing, when we are dealing with partial derivatives in linear algebra we will come across sparse data.

# How to Work With Sparse Data
# SciPy has a module, scipy.sparse that provides functions to deal with sparse data.
# There are primarily two types of sparse matrices that we use:
# CSC - Compressed Sparse Column. For efficient arithmetic, fast column slicing.
# CSR - Compressed Sparse Row. For fast row slicing, faster matrix vector products
# We will use the CSR matrix in this tutorial.
# CSR Matrix
# We can create CSR matrix by passing an arrray into function scipy.sparse.csr_matrix().
# Create a CSR matrix from an array:

import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])

print(csr_matrix(arr))


# From the result we can see that there are 3 items with value.
# The 1. item is in row 0 position 5 and has the value 1.
# The 2. item is in row 0 position 6 and has the value 1.
# The 3. item is in row 0 position 8 and has the value 2.

# sparse Matrix Methods
# Viewing stored data (not the zero items) with the data property:

import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
print(csr_matrix(arr).data)


#Counting nonzeros with the count_nonzero() method:
import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
print(csr_matrix(arr).count_nonzero())

#Removing zero-entries from the matrix with the eliminate_zeros() method:
import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
mat = csr_matrix(arr)
mat.eliminate_zeros()
print(mat)

#Eliminating duplicates by adding them:

import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
mat = csr_matrix(arr)
mat.sum_duplicates()
print(mat)

#Converting from csr to csc with the tocsc() method:

import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
newarr = csr_matrix(arr).tocsc()
print(newarr)