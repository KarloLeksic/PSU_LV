import matplotlib.image as mpimg
import scipy as sp
from sklearn import cluster, datasets
import numpy as np
import matplotlib.pyplot as plt

imageNew = mpimg.imread('example.png')

X = imageNew.reshape((-1, 1)) # We need an (n_sample, n_feature) array
red = X[:, :, 0]
k_means = cluster.KMeans(n_clusters=10,n_init=1)
k_means.fit(X) 
values = k_means.cluster_centers_.squeeze()
labels = k_means.labels_
imageNew_compressed = np.choose(labels, values)
imageNew_compressed.shape = imageNew.shape


plt.figure(1)
plt.imshow(imageNew)
plt.show()

plt.figure(2)
plt.imshow(imageNew_compressed,  cmap='gray')
plt.show()