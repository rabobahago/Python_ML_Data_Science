# Reshaping arrays
# Reshaping means changing the shape of an array.
# The shape of an array is the number of elements in each dimension.
# By reshaping we can add or remove dimensions or change number of elements in each dimension.

# Convert the following 1-D array with 12 elements into a 2-D array.
# The outermost dimension will have 4 arrays, each with 3 elements:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

# Convert the following 1-D array with 12 elements into a 3-D array.

# The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)
#Check if the returned array is a copy or a view:

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base)

#Convert 1D array with 8 elements to 3D array with 2x2 elements:

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)

# Flattening the arrays
# Flattening array means converting a multidimensional array into a 1D array.
# We can use reshape(-1) to do this.
# Convert the array into a 1D array:

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)
# Note: There are a lot of functions for changing the shapes of arrays in
# numpy flatten, ravel and also for rearranging the elements rot90, flip,
# fliplr, flipud etc. These fall under Intermediate to Advanced section of numpy.