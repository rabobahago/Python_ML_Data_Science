# Hierarchical Clustering
# Hierarchical clustering is an unsupervised learning method for clustering data points.
# The algorithm builds clusters by measuring the dissimilarities between data.
# Unsupervised learning means that a model does not have to be trained, and we do not need a "target" variable.
# This method can be used on any data to visualize and interpret the relationship between individual data points.

# Here we will use hierarchical clustering to group data points and visualize the clusters using both a dendrogram and scatter plot.
# How does it work?
# We will use Agglomerative Clustering, a type of hierarchical clustering that follows
# a bottom up approach. We begin by treating each data point as its own cluster. Then,
# we join clusters together that have the shortest distance between them to create larger
# clusters. This step is repeated until one large cluster is formed containing all of the data points.
# Hierarchical clustering requires us to decide on both a distance and linkage method.
# We will use euclidean distance and the Ward linkage method, which attempts to minimize the variance between clusters.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering

x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

data = list(zip(x, y))

hierarchical_cluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')
labels = hierarchical_cluster.fit_predict(data)

plt.scatter(x, y, c=labels)
plt.show()