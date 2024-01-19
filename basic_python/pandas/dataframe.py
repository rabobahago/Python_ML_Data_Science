# What is a DataFrame?
# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a
# table with rows and columns.
# Create a simple Pandas DataFrame:

import pandas as pd
df = pd.DataFrame({
    "Name":["Rabo Yusuf", 'Martins Shuka', 'Mart Kenneth'],
    "Age": [30, 34, 45],
    "Sex":['Male', 'Female', 'Female']
    })
print(df['Age'])
# I’m just interested in working with the data in the column Age
df['Age']
print(df['Age'].max())
# I’m interested in some basic statistics of the numerical data of my data table
print(df['Age'].describe())
print(df['Age'].describe()[''])
# You can create a Series from scratch as well:
age = pd.Series([23, 45, 67, 90], name='Age')
print(age)
print(age.max())
