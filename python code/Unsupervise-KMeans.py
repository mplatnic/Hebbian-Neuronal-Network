# this file for Python3 uses sklearn library to calculate clusters depending on entries
# the idea if to classify Data into different groups of data named Clusters.
# Unsupervised artificial intelligence algorithm is used to determine the center of the clusters

import matplotlib.pyplot as plt       #for visualization
from matplotlib import style
import numpy as np                    #mattrix
from sklearn.cluster import KMeans    #core of the ANN
style.use('ggplot')

X = np.array([[1, 2],
              [1.5, 1.8],
              [5, 8],
              [8, 8],
              [1, 0.6],
              [9, 11]])


plt.scatter(X[:, 0],X[:, 1], s=15, linewidths = 5, zorder = 5)    #prepare for data visualization
plt.show()                  #visualize data

clf = KMeans(n_clusters=2)    # choose that data is classified in 2 clusters
clf.fit(X)

centroids = clf.cluster_centers_    #center of each cluster
labels = clf.labels_                #number of each cluster

colors = ["g.","r.","c.","y."]
for i in range(len(X)):
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)
plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)
plt.show()
