import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 3, 3, 2, 1])
y = np.array([1, 1 ,2, 2, 1])
plt.title('Prvi plt')
plt.plot(x, y, linewidth = 1, marker = "o")
plt.axis([0, 4, 0, 4])
plt.xlabel("X os")
plt.ylabel("Y os")
plt.show()