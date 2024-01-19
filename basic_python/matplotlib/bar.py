# Creating Bars
# With Pyplot, you can use the bar() function to draw bar graphs:
# Draw 4 bars:

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()

# Horizontal Bars
# If you want the bars to be displayed horizontally instead of vertically, use the barh() function:
# Draw 4 horizontal bars:

import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.barh(x, y)
plt.show()

# Bar Color
# The bar() and barh() take the keyword argument color to set the color of the bars:
# Draw 4 red bars:

import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x, y, color = "red")
plt.show()