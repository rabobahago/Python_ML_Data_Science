# Define a function called step_gradient() that takes in x, y, b_current, and m_current.
# This function will find the gradients at b_current and m_current,
# and then return new b and m values that have been moved in that direction.
# For now, just return the pair (b_current, m_current).
# Inside step_gradient(), find the gradient at b_current and the gradient at
# m_current using the functions defined before (get_gradient_at_b and get_gradient_at_m).
# Store these gradients in variables called b_gradient and m_gradient,
# and return these from the function instead of b_current and m_current.
# Return them as a list.
# Let’s try to move the parameter values in the direction of the gradient at a rate of 0.01.
# Create variables called b and m:
# b should be b_current - (0.01 * b_gradient)
# m should be m_current - (0.01 * m_gradient)
# Return the pair b and m from the function.
# We have provided Sandra’s lemonade data once more. We have a guess for what we think the b and m might be.
# Call your function to perform one step of gradient descent. Store the results in the variables b and m.
# Great! We have a way to step to new b and m values! Next, we will call this function a bunch,
#in order to move those values towards lower and lower loss.

def get_gradient_at_b(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
    x_val = x[i]
    y_val = y[i]
    diff += (y_val - ((m * x_val) + b))
  b_gradient = -(2/N) * diff
  return b_gradient

def get_gradient_at_m(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
      x_val = x[i]
      y_val = y[i]
      diff += x_val * (y_val - ((m * x_val) + b))
  m_gradient = -(2/N) * diff
  return m_gradient

def step_gradient(x, y, b_current, m_current):
  b_gradient = get_gradient_at_b(x, y, b_current, m_current)
  b = b_current - (0.01 * b_gradient)
  m_gradient = get_gradient_at_m(x, y, b_current, m_current)
  m = m_current - (0.01 * m_gradient)
  return(b, m)

# Define your step_gradient function here

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]


# current intercept guess:
b = 0
# current slope guess:
m = 0
b, m = step_gradient(months, revenue, b, m)
print(b, m)
# Call your function here to update b and m
