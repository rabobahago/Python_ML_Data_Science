# Understand Data with Visualization
# Scatter plot matrix
import matplotlib.pyplot as plt
import pandas
from pandas.plotting import scatter_matrix

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)
# Use the hist() function to create a histogram of each attribute.
scatter_matrix(data)
# Use the plot(kind=’box’) function to create box-and-whisker plots of each attribute
data.hist()
# Use the pandas.scatter_matrix() function to create pairwise scatterplots of all attributes.
data.plot(kind='box')
plt.show()