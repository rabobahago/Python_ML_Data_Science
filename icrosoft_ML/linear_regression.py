import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, model_selection
X, y = datasets.load_diabetes(return_X_y=True)
X = X[:, 2]
X = X.reshape((-1, 1))
# split the dataset: 70% and 30%
X_train, X_test, y_train, y_test = model_selection.train_test_split(
    X, y, test_size=0.33)
# Get Linear Regression by importing linear model
model = linear_model.LinearRegression()
# train our model by fit X_train, y_train
model.fit(X_train, y_train)
# predict y_pred from X_test
y_pred = model.predict(X_test)
plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.ylabel('Disease Progression')
plt.title('A Graph Plot Showing Diabetes Progression Against BMI')
plt.show()
