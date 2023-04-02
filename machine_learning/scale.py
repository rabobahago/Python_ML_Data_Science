# The task in the Multiple Regression chapter was to predict the CO2 emission from a car
# when you only knew its weight and volume.
# When the data set is scaled, you will have to use the scale when you predict values:
# Predict the CO2 emission from a 1.3 liter car that weighs 2300 kilograms:
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

scaledX = scale.fit_transform(X)

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])

predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)