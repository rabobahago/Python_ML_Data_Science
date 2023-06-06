import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('./birds.csv')
print(birds.head())
# wingspan = birds['MaxWingspan']
# wingspan.plot()
# plt.title('Max Wingspan in Centimeters')
# plt.ylabel('Wingspan (CM)')
# plt.xlabel('Birds')
# plt.xticks(rotation=45)
# x = birds['Name']
# y = birds['MaxWingspan']
# plt.plot(x, y)


# plt.title('Max Wingspan in Centimeters')
# plt.ylabel('Wingspan (CM)')
# plt.tick_params(axis='both', which='both', labelbottom=False, bottom=False)
print('........')
for i in range(len(birds)):
    x = birds["Name"][i]
    y = birds['MaxWingspan'][i]
    plt.plot(x, y, 'bo')
    if birds['MaxWingspan'][i] > 500:
        plt.text(x, y * (1 - 0.005), birds['Name'][i], fontsize=12)
plt.show()

# Filter your data
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.xlabel('Birds')
plt.tick_params(axis='both', which='both', labelbottom=False, bottom=False)
for i in range(len(birds)):
    x = birds['Name'][i]
    y = birds['MaxWingspan'][i]
    # here go the filter
    if birds['Name'][i] not in ['Bald eagle', 'Prairie falcon']:
        plt.plot(x, y, 'bo')
plt.show()

# Explore bar charts
birds.plot(x='Category',
           kind='bar',
           stacked=True,
           title='Birds of Minnesota')
category_count = birds.value_counts(birds['Category'].values, sort=True)
plt.rcParams['figure.figsize'] = [6, 12]
category_count.plot.barh()
plt.show()
