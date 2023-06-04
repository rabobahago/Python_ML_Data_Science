import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
example1 = pd.Series([0, np.nan, '', None])
# print(df.head())
# print(df.tail())
# print(df.info())
# print(example1.isnull())
# print(example1.notnull())
# None
# 0    False
# 1     True
# 2    False
# 3     True
# dtype: bool
# row is observations
# columns is variables
example2 = pd.DataFrame([[np.nan, 3, 6], [5, 8, 90], [6, 80, np.nan]])
print(example2.dropna())
print('.....')
print(example2.dropna(axis=1))
# set additional row 3 with all values to be NaN
example2[3] = np.nan
print(example2)
print('all')
# leave only columns with three or more nonull value
print(example2.dropna(axis=1, thresh=3))
# leave only rows with three or more nonull value
print(example2.dropna(axis=0, thresh=3))
print(example2.dropna(how='all'))

# fill all NaN in a table
sr = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
print(sr)
# fill nan value by passing the value
print(sr.fillna(0))
# fill nan by forward method
print(sr.fillna(method='ffill'))
# fill nan by backward method
print(sr.fillna(method='bfill'))

print(example2.fillna(method='ffill', axis=1))

# duplicate
df = pd.DataFrame({"letters": ["A", 'B'] * 2 +
                  ['B'], 'values': [1, 3, 4, 5, 6]})
print(df.duplicated())
print(df.drop_duplicates())
