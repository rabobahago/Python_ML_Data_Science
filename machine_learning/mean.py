# Machine Learning is making the computer learn from studying data and statistics.
# Machine Learning is a step into the direction of artificial intelligence (AI).
# Machine Learning is a program that analyses data and learns to predict the outcome.

# Data Set
# In the mind of a computer, a data set is any collection of data. It can be anything from an array to a complete database.
# Example of an array:
# [99,86,87,88,111,86,103,87,94,78,77,85,86]

# Data Types
# To analyze data, it is important to know what type of data we are dealing with.
# We can split the data types into three main categories:
# 1) Numerical
# 2) Categorical
# 3) Ordinal

# Numerical data are numbers, and can be split into two numerical categories:
# Discrete Data
# - numbers that are limited to integers. Example: The number of cars passing by.
# Continuous Data
# - numbers that are of infinite value. Example: The price of an item, or the size of an item
# Categorical data are values that cannot be measured up against each other. Example: a color value, or any yes/no values.
# Ordinal data are like categorical data, but can be measured up against each other. Example: school grades where A is better than B and so on.
# By knowing the data type of your data source, you will be able to know what technique to use when analyzing them.

# What can we learn from looking at a group of numbers?

# In Machine Learning (and in mathematics) there are often three values that interests us:
# Mean - The average value
# Median - The mid point value
# Mode - The most common value
# Example: We have registered the speed of 13 cars:
# speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# What is the average, the middle, or the most common speed value?
import numpy
from scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
m = numpy.mean(speed)
print(m)
med = numpy.median(speed)
print(med)
#set keepdims = True to ignore a warning
mod = stats.mode(speed, keepdims=True)
#In order to access the mod you will need to get the first element in the mode return
#the first element in the tuple
print(mod[0][0])