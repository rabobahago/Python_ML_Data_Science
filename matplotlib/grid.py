import matplotlib.pyplot as plt
import numpy as np

xpoint = np.array([1, 4, 7, 9, 11])
ypoint = np.array([20, 40, 50, 60,70])
plt.title("US Cars", loc='center')
plt.xlabel("Percentage")
plt.ylabel("Number of cars")
plt.grid(axis='y', color='red', linestyle='--')
plt.plot(xpoint, ypoint)
plt.show()