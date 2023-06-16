

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
# read from CSV File
pumpkins = pd.read_csv('./pumpkins.csv')

pumpkins = pumpkins[pumpkins['Package'].str.contains(
    'bushel', case=True, regex=True)]
# check for null and sum for column
pumpkins.isnull().sum()
# select specific columns
columns_to_select = ['Package', 'Low Price', 'High Price', 'Date']
# select all rows of the selected columns
pumpkins = pumpkins.loc[:, columns_to_select]
# Average price of pumpkins
price = (pumpkins['Low Price'] + pumpkins['High Price']) / 2
# Month
month = pd.DatetimeIndex(pumpkins['Date']).month

day_of_year = pd.to_datetime(pumpkins['Date']).apply(
    lambda dt: (dt-datetime(dt.year, 1, 1)).days)

# copy your converted data into a fresh Pandas dataframe

new_pumpkins = pd.DataFrame(
    {'Month': month, 'Package': pumpkins['Package'], 'Low Price': pumpkins['Low Price'], 'High Price': pumpkins['High Price'], 'Price': price})
new_pumpkins.loc[new_pumpkins['Package'].str.contains(
    '1 1/9'), 'Price'] = price/(1 + 1/9)

new_pumpkins.loc[new_pumpkins['Package'].str.contains(
    '1/2'), 'Price'] = price/(1/2)
price = new_pumpkins.Price
month = new_pumpkins.Month
plt.scatter(price, month)
plt.show()

new_pumpkins.groupby(['Month'])['Price'].mean().plot(kind='bar')
plt.ylabel("Pumpkin Price")
print(new_pumpkins['Month'].corr(new_pumpkins['Price']))
print(new_pumpkins['DayOfYear'].corr(new_pumpkins['Price']))
ax = None
colors = ['red', 'blue', 'green', 'yellow']
for i, var in enumerate(new_pumpkins['Variety'].unique()):
    df = new_pumpkins[new_pumpkins['Variety'] == var]
    ax = df.plot.scatter('DayOfYear', 'Price', ax=ax, c=colors[i], label=var)
pipeline = make_pipeline(PolynomialFeatures(2), LinearRegression())
