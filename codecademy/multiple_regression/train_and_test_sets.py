# In general, putting 80% of your data in the training set and 20% of your data in the test set is a good place to start.
# Suppose you have some values in x and some values in y:
# from sklearn.model_selection import train_test_split
# x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2)
# Here are the parameters:
# train_size: the proportion of the dataset to include in the train split (between 0.0 and 1.0)
# test_size: the proportion of the dataset to include in the test split (between 0.0 and 1.0)
# random_state: the seed used by the random number generator [optional]
# To learn more, here is a Training Set vs Validation Set vs Test Set article.

#import from pandas
import pandas as pd
#import from matplotlib
import matplotlib.pyplot as plt
#Import LinearRegression from scikit-learn’s linear_model module.
from sklearn.linear_model import LinearRegression
# Import train_test_split from sklearn.model_selection.
from sklearn.model_selection import train_test_split
#data manhattan.csv
streeteasy = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/manhattan.csv")

df = pd.DataFrame(streeteasy)
print(df)

# Create a DataFrame x that selects the following columns from the main df DataFrame:
# 'bedrooms'
# 'bathrooms'
# 'size_sqft'
# 'min_to_subway'
# 'floor'
# 'building_age_yrs'
# 'no_fee'
# 'has_roofdeck'
# 'has_washer_dryer'
# 'has_doorman'
# 'has_elevator'
# 'has_dishwasher'
# 'has_patio'
# 'has_gym'
# Create a DataFrame y that selects the rent column from the main df DataFrame.
# These are the columns we want to use for our regression model.

x = df[['bedrooms', 'bathrooms', 'size_sqft', 'min_to_subway', 'floor', 'building_age_yrs', 'no_fee', 'has_roofdeck', 'has_washer_dryer', 'has_doorman', 'has_elevator', 'has_dishwasher', 'has_patio', 'has_gym']]
y = df['rent']

# Use scikit-learn’s train_test_split() method to split x into 80% training set and 20% testing set and generate:
# x_train
# x_test
# y_train
# y_test
# Set the random_state to 6.

(x_train, x_test, y_train, y_test) = train_test_split(x, y, train_size = 0.8, test_size = 0.2, random_state = 6)

# Let’s take a look at the shapes of x_train, x_test, y_train, and y_test to see we got the proportion we wanted.
# We have 14 features that we’re looking for for each apartment, and 1 label we’re looking for for each apartment.
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

# Create a Linear Regression model and call it mlr.
# Fit the model using x_train and y_train.
mlr = LinearRegression()
mlr.fit(x_train, y_train)

# Print out the coefficients using .coef_.
print(mlr.coef_)
# Use the model to predict y-values from x_test. Store the predictions in a variable called y_predict.
# Now we have:
# x_test
# x_train
# y_test
# y_train
# and y_predict!
y_predict = mlr.predict(x_test)

#just a test data created randomly
rabo_apartment = [[1, 1, 500, 15, 1, 88, 1, 0,1, 0, 1, 0, 1, 0]]
predict = mlr.predict(rabo_apartment)
print('Predicted rent: $%.2f' % predict)

# Create a 2D scatter plot using y_test and y_predict.
# The x-axis should represent actual rent prices and the y-axis should represent predicted rent prices.
plt.xlabel('Independ. Variable')
plt.ylabel('Price')
plt.title('Price VS Ind. variable')
#Create a scatterplot of size_sqft and rent:
plt.scatter(df[['size_sqft']], df[['rent']], alpha=0.4)
#Create a scatterplot of min_to_subway and rent:
plt.scatter(df[['min_to_subway']], df[['rent']], alpha=0.4)

# Use the .score() method from LinearRegression to find the mean squared error regression loss for the testing set.
# Write that number down.
print("Test score:")
print(mlr.score(x_test, y_test))

# Use the .score() method from LinearRegression to find the mean squared error regression loss for the training set.
# Write that number down.
print("Train score:")
print(mlr.score(x_train, y_train))
plt.show()
