# Understand Data with Descriptive Statistics

import pandas
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)

# Understand your data using the head() function to look at the first few rows.
print(data.head())

# Review the dimensions of your data with the shape property.
print(data.shape)

#Look at the data types for each attribute with the dtypes property.
print(data['preg'].dtype)
print(data['plas'].dtype)
print(data['pres'].dtype)
print(data['skin'].dtype)
print(data['test'].dtype)
print(data['mass'].dtype)
print(data['pedi'].dtype)
print(data['age'].dtype)
print(data['class'].dtype)

# Review the distribution of your data with the describe() function.
description = data.describe()
print(description)

# Calculate pairwise correlation between your variables using the corr() function.
print(data.corr())