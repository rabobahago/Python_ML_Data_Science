# Define a function called get_gradient_at_m() that takes
# in a set of x values, x, a set of y values, y, a slope m, and an intercept value b.
# For now, have it return m.

# In this function, we want to go through all of the x values
# and all of the y values and compute x*(y - (m*x+b)) for each of them.
# Create a variable called diff that has the sum of all of these values, and return it from the function.
# Define a variable called m_gradient and set it equal to the -2/N multiplied by diff.
# Instead of returning diff, return m_gradient

def get_gradient_at_m(x, y, m, b):
    diff = 0
    N = len(x)
    for i in range(N):
      y_val = y[i]
      x_val = x[i]
      diff += x_val*(y_val - ((m * x_val) + b))
    m_gradient = -2/N * diff
    return m_gradient