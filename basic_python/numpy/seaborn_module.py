# Visualize Distributions With Seaborn
# Seaborn is a library that uses Matplotlib underneath to plot graphs.
# It will be used to visualize random distributions.

import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([0, 1, 2, 3, 4, 5])
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
plt.show()