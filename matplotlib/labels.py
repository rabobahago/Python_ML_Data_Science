import matplotlib.pyplot as plt
import numpy as np

xpoint = np.array([2, 5, 6, 7, 12, 34])
ypoint = np.array([20, 50, 70, 120, 130, 160])
font1 = {"family": "serif", "size":20, 'color':'green'}
font2 = {"family": "serif", "size":10, 'color':'green'}
plt.plot(xpoint, ypoint)
plt.title('Nigeria Government', loc='left',fontdict= font1)
plt.xlabel('Average Salaries', fontdict= font2)
plt.ylabel('Year of Services', fontdict= font2)
plt.show()