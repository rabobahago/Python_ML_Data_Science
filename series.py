import pandas as pd
a = pd.Series(range(1, 10))
b = pd.Series(["I", "like", "to", "play", "games", "and",
              "will", "not", "change"], index=range(0, 9))
c = pd.DataFrame([a, b])
columns = pd.DataFrame({"A": a, "B": b})
df = pd.DataFrame([a, b]).T.rename(columns={0: "A", 1: "B"})
another = df[['A', 'B']]
print(another[(another["A"] > 5) & (another["B"] == 'and')])
df["DivA"] = df["A"] - df["A"].mean()
df['LenB'] = df["B"].apply(lambda x: len(x))
df['Add'] = 2 + df['B'].apply(len)
print(df)
