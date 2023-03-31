# Histogram
# To visualize the data set we can draw a histogram with the data we collected.
# We will use the Python module Matplotlib to draw a histogram.
import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
plt.show()