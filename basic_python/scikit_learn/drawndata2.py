from sklearn.neighbors import KNeighborsRegressor
import pandas as pd
import matplotlib.pylab as plt
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import PolynomialFeatures, OneHotEncoder
from sklearn.pipeline import Pipeline
import numpy as np
df =pd.read_csv('drawndata2.csv')
df.head(3)
X = df[['x', 'y']].values
y = df[['z']] == 'a'
from sklearn.preprocessing import StandardScaler, QuantileTransformer
X_new = QuantileTransformer(n_quantiles=100).fit_transform(X)
plt.scatter(X_new[:, 0], X_new[:, 1])
array = np.array(['low', 'low', 'high', 'medium']).reshape(-1, 1)
enc = OneHotEncoder(sparse=False, handle_unknown='ignore')
enc.fit_transform(array)
enc.transform(np.array(['z']).reshape(-1, 1))
