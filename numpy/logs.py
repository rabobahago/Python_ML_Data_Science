# Logs
# NumPy provides functions to perform log at the base 2, e and 10.
# We will also explore how we can take log for any base by creating a custom ufunc.
# All of the log functions will place -inf or inf in the elements if the log can not be computed.
import numpy as np
range = np.arange(1, 10)
print(np.log2(range))
print(np.log10(range))
print(np.log(range))

from math import log
import numpy as np
nplog = np.frompyfunc(log, 2, 1)
print(nplog(100, 15))