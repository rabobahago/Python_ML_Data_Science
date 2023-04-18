import pandas as pd
df = pd.read_csv('honeyproduction.csv')
#get single col
totalprod = df['totalprod']
print(totalprod)
#get multiple cols
totalprod_stocks = df[['totalprod', 'stocks']]
print(totalprod_stocks.head(20))
#filter a specific row
stocks_num = df[df['stocks'] == 159000][['stocks', 'totalprod']]
print(stocks_num.shape)
row = df[['stocks', 'totalprod']].isin([1, 2])
print(row)
print(df.loc[df.index < 5, "totalprod"])
print(df)
df['yield'] = df['yieldpercol'] + 100
print(df.head())