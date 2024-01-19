# Create Histogram
# In Matplotlib, we use the hist() function to create histograms.
# The hist() function will use an array of numbers to create a
# histogram, the array is sent into the function as an argument.
# For simplicity we use NumPy to randomly generate an array with 250
# values, where the values will concentrate around 170, and the standard deviation is 10.
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(270, 10, 250)
plt.hist(x)
plt.show()