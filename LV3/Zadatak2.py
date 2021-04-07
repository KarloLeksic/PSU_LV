import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

mtcars = pd.read_csv('mtcars.csv') 

mt4 = mtcars[(mtcars.cyl == 4)].mean()
mt6 = mtcars[(mtcars.cyl == 6)].mean()
mt8 = mtcars[(mtcars.cyl == 8)].mean()

label = ["4 cilindra", "6 cilindra", "8cilindra"]
values = [mt4.mpg, mt6.mpg, mt8.mpg]

plt.bar(label, values)
plt.ylabel("MPG")
plt.show()