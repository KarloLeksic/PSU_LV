import numpy as np
import matplotlib.pyplot as plt

bacanje = np.zeros((100, 1))

for i in range(0, 100):
    bacanje[i] = np.random.randint(1, 7)
    
print (bacanje)

plt.hist(bacanje, bins = 6, rwidth = 0.9) #nije dobar, treba poboljsat
plt.show()