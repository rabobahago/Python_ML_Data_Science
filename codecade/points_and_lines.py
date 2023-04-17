import matplotlib.pyplot as plt
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

#slope:
m = 8
#intercept:
b = 40


#change to fit
m = 10
b = 45
# We have provided a slope, m, and an intercept, b, that seems to describe the revenue data you have been given.
# Create a new list, y, that has every element in months, multiplied by m and added to b.
# A list comprehension is probably the easiest way to do this!

y = [m * x_value + b for x_value in months]

# Plot the y values against months as a line on top of the
# scatterplot that was plotted with the line plt.plot(months, revenue, "o").
plt.plot(months, revenue, "o")
# Change m and b to the values that you think match the data the best.
# What does the slope look like it should be? And the intercept?
plt.plot(months, y)
plt.show()
