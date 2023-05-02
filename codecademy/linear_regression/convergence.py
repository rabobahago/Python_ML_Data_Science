# Run the file. Look at the graph. This graph shows how much
# the parameter b changed with each iteration of a gradient descent runner.
# How many iterations did it take for this program to converge?
# Enter your answer in a variable called num_iterations.
# At what b value did this program converge?
# Enter your answer in a variable called convergence_b

import matplotlib.pyplot as plt
from data import bs, bs_000000001, bs_01

iterations = range(1400)

plt.plot(iterations, bs)
plt.xlabel("Iterations")
plt.ylabel("b value")
plt.show()
num_iterations = 800
convergence_b = 45