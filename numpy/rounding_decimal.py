# Rounding Decimals
# There are primarily five ways of rounding off decimals in NumPy:
# truncation
# fix
# rounding
# floor
# ceil
# Truncation
# Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.
#Truncate elements of following array:

import numpy as np
trunc = np.trunc([-3.1666, 3.6667])
around = np.round([-3.1666, 3.6667])
floor = np.floor([-3.1666, 3.6667])
ceil = np.ceil([-3.1666, 3.6667])
print(trunc)
print(around)
print(floor)
print(ceil)