import pandas as pd
df = pd.read_csv('honeyproduction.csv')
print(df.head(8))
print(df.tail(8))
print(df.dtypes)
print(df.info())