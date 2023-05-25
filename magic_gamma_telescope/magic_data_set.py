import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
cols = ['fLength', 'fWidth', 'fSize', 'fConc', 'fConc1', 'fAsym', 'fM3Long', 'fM3Trans', 'fAlpha', 'fDist', 'class']
df = pd.read_csv("magic04.data", names=cols)
df['class'] = (df['class'] == 'g').astype(int)
df.head()
for label in cols[:-1]:
    plt.hist(df[df['class']== 1][label], color='blue', label='gamma', alpha = 0.7, density = True)
    plt.hist(df[df['class']== 0][label], color='red', label='latron', alpha = 0.7, density = True)
    plt.title(label)
    plt.ylabel('Probability')
    plt.xlabel(label)
    plt.legend()
    plt.show()