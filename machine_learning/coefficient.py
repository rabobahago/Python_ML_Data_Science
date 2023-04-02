# Coefficient
# The coefficient is a factor that describes the relationship with an unknown variable.
# Example: if x is a variable, then 2x is x two times. x is the unknown variable, and the number 2 is the coefficient.
# In this case, we can ask for the coefficient value of weight against CO2, and for volume against CO2.
# The answer(s) we get tells us what would happen if we increase, or decrease, one of the independent values.


import pandas
from sklearn import linear_model

df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

print(regr.coef_)