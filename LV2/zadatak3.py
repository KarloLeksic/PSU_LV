import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("mtcars.csv", "rb"), usecols = (1, 2, 3, 4, 5, 6), delimiter = ",", skiprows = 1)

mpg = data[:, 0]

print(mpg)

#plt.scatter(d)
#plt.show()
