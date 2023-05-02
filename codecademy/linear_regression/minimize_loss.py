# Define a function called get_gradient_at_b() that takes in
# a set of x values, x, a set of y values, y, a slope m, and an intercept value b.
# For now, have it return b, unchanged.
# In the get_gradient_at_b() function, we want to go through
# all of the x values and all of the y values and compute (y - (m*x+b)) for each of them.
# Create a variable called diff that has the sum of all of these values.
# Instead of returning b from the get_gradient_at_b() function, return diff

# Still in the get_gradient_at_b() function, define a variable
# called b_gradient and set it equal to the -2/N multiplied by diff.
# Note: N is the number of points, i.e. the length of the x list or the y list.
# Instead of returning diff, return b_gradient.

def get_gradient_at_b(x, y, m,b):
  diff = 0
  N = len(x)
  for i in range(len(x)):
    y_val = y[i]
    x_val = x[i]
    diff += (y_val - (m * x_val + b))
    b_gradient = diff * ((-2)/N)
  return b_gradient