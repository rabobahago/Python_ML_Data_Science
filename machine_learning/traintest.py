# Evaluate Your Model
# In Machine Learning we create models to predict the outcome of certain events,
# like in the previous chapter where we predicted the CO2 emission of a car when we knew the weight and engine size.
# To measure if the model is good enough, we can use a method called Train/Test.
# What is Train/Test
# Train/Test is a method to measure the accuracy of your model.
# It is called Train/Test because you split the data set into two sets: a training set and a testing set.
# 80% for training, and 20% for testing.
# You train the model using the training set.
# You test the model using the testing set.
# Train the model means create the model.
# Test the model means test the accuracy of the model.
# tart With a Data Set
# Start with a data set you want to test.

# Our data set illustrates 100 customers in a shop, and their shopping habits.

import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

myline = numpy.linspace(0, 6, 100)

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()

# R2
# Remember R2, also known as R-squared?
# It measures the relationship between the x axis and the y axis,
# and the value ranges from 0 to 1, where 0 means no relationship, and 1 means totally related.
# The sklearn module has a method called r2_score() that will help us find this relationship.
# In this case we would like to measure the relationship between the minutes a customer stays in
# the shop and how much money they spend.

import numpy
from sklearn.metrics import r2_score
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]
mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
r2 = r2_score(train_y, mymodel(train_x))
print(r2)

# Bring in the Testing Set
# Now we have made a model that is OK, at least when it comes to training data.

# Now we want to test the model with the testing data as well, to see if gives us the same result.

# Example
# Let us find the R2 score when using testing data:

import numpy
from sklearn.metrics import r2_score
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
r2 = r2_score(test_y, mymodel(test_x))
print(r2)