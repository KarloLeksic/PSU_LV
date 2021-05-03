from sklearn import datasets, cluster
import numpy as np
import matplotlib.pyplot as plt

def generate_data(n_samples, flagc):
    
    if flagc == 1:
        random_state = 365
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        
    elif flagc == 2:
        random_state = 148
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
        X = np.dot(X, transformation)
        
    elif flagc == 3:
        random_state = 148
        X, y = datasets.make_blobs(n_samples=n_samples,
                                    centers=4,
                                    cluster_std=[1.0, 2.5, 0.5, 3.0],
                                    random_state=random_state)

    elif flagc == 4:
        X, y = datasets.make_circles(n_samples=n_samples, factor=.5, noise=.05)
        
    elif flagc == 5:
        X, y = datasets.make_moons(n_samples=n_samples, noise=.05)
    
    else:
        X = []
        
    return X


data = generate_data(500, 1)
plt.figure(1)
plt.scatter(data[:, 0], data[:, 1])
plt.show()

k_means = cluster.KMeans(3).fit(data)

label0 = data[k_means.labels_ == 0]
label1 = data[k_means.labels_ == 1]
label2 = data[k_means.labels_ == 2]

#centri
values = k_means.cluster_centers_.squeeze()

plt.scatter(label0[:, 0], label0[:, 1], color = "red")
plt.scatter(label1[:, 0], label1[:, 1], color = "blue")
plt.scatter(label2[:, 0], label2[:, 1], color = "green")
plt.scatter(values[:, 0], values[:, 1], marker = 'X', color = 'black')
plt.show()