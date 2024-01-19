# Creating Pie Charts
# With Pyplot, you can use the pie() function to draw pie charts:

# Start the first wedge at 90 degrees:
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels, startangle = 90)
plt.show()

x = np.array([40, 7, 5, 8, 10, 20])
mylabels = ["Apples", "Bananas", "Cherries", "Mango", 'Others', 'Cashew']
myexplode = [0.3, 0, 0, 0, 0, 0.2]
plt.pie(x, labels = mylabels,  explode = myexplode)
plt.legend(title='Fruits Six')
plt.show()