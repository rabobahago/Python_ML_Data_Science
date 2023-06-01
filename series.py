import pandas as pd
a = pd.Series(range(1, 10))
b = pd.Series(["I", "like", "to", "play", "games", "and",
              "will", "not", "change"], index=range(0, 9))
c = pd.DataFrame([a, b])
columns = pd.DataFrame({"A": a, "B": b})
print(columns)
transponse = pd.DataFrame([a, b]).T.rename(columns={0: "A", 1: "B"})
print(transponse)
