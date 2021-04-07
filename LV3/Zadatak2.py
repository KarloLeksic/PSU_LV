import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

mtcars = pd.read_csv('mtcars.csv') 

mt4 = mtcars[(mtcars.cyl == 4)].mean()
mt6 = mtcars[(mtcars.cyl == 6)].mean()
mt8 = mtcars[(mtcars.cyl == 8)].mean()

label_cyl = ["4 cilindra", "6 cilindra", "8cilindra"]
values_mpg = [mt4.mpg, mt6.mpg, mt8.mpg]


plt.bar(label_cyl, values_mpg)
plt.ylabel("MPG")
plt.show()

boxplot = mtcars.boxplot()
plt.show()