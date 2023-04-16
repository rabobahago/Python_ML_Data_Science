# Creating Scatter Plots
# With Pyplot, you can use the scatter() function to draw a scatter plot.
# The scatter() function plots one dot for each observation. It needs two arrays
# of the same length, one for the values of the x-axis, and one for values on the y-axis:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([2, 1, 5, 10, 23, 3, 4, 8])
y = np.array([120, 130, 80, 33, 20, 98, 60, 39])

plt.scatter(x, y)
plt.show()

# The observation in the example above is the result of 13 cars passing by.
# The X-axis shows how old the car is.
# The Y-axis shows the speed of the car when it passes.
# Are there any relationships between the observations?
# It seems that the newer the car, the faster it drives, but that could be
# a coincidence, after all we only registered 13 cars.

# Compare Plots
# In the example above, there seems to be a relationship between speed and age, but what if
# we plot the observations from another day as well? Will the scatter plot tell us something else?
# Draw two plots on the same figure:

import matplotlib.pyplot as plt
import numpy as np

#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)

plt.show()


# Set your own color of the markers:

import matplotlib.pyplot as plt
import numpy as np
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
plt.scatter(x, y, c=colors)
plt.show()