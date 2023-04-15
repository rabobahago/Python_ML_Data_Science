import matplotlib.pyplot as plt
import numpy as np

xpoint = np.array([2, 5, 6, 7, 12, 34])
ypoint = np.array([20, 50, 70, 120, 130, 160])
plt.plot(xpoint, ypoint)
plt.xlabel('Average Salaries')
plt.ylabel('Year of Services')
plt.show()