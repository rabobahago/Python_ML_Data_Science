# We have imported two new lists representing how the b value changed with different learning rates:
# bs_000000001: 1400 iterations of gradient descent on b with a learning rate of 0.000000001
# bs_01: 100 iterations of gradient descent on b with a learning rate of 0.01
# Change the plot to plot bs_000000001 instead of bs.
# Does the gradient descent algorithm still converge to the same b value?
# Does it converge at all? Look at the values on the y-axis!

# Change the plot to plot bs_01 instead of bs_000000001.
# Unfortunately, our computers blew up after 100 iterations of this,
# so you’ll also have to change the number of iterations to 100 instead of 1400:
# iterations = range(100)
#Does the gradient descent algorithm still converge to the same b value? Does it converge at all?
import matplotlib.pyplot as plt
from data import bs, bs_000000001, bs_01

iterations = range(100)

plt.plot(iterations, bs_01)
plt.xlabel("Iterations")
plt.ylabel("b value")
plt.show()
num_iterations = 800
convergence_b = 45