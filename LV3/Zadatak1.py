import pandas as pd 
import numpy as numpy

mtcars = pd.read_csv('mtcars.csv') 
print(len(mtcars)) 
print(mtcars)

#5 s najvecom potrosnjom
mtcars.sort_values(by = ["mpg"], inplace = True)
print(mtcars.head(5))

#3 automobila s 8 cilindara s najmanjom potrosnjom
mtcars.sort_values(by = ["mpg"], inplace = True,  ascending = False)
print(mtcars[(mtcars.cyl == 8)].head(3))

#srednja potrosnja automobila sa 6 cilindara
mt6 = mtcars[(mtcars.cyl == 6)]
print(mt6["mpg"].mean())

#srednja potrosnja 4 cilindra mase 2000 - 2200 lbs
mt4 = mtcars[(mtcars.cyl == 4) & (mtcars.wt >= 2) & (mtcars.wt <= 2.2)]
print(mt4["mpg"].mean())

#kolko ima automatski mjenjac, a kolko rucni
print("Automatski mjenjac: ", mtcars[mtcars.am == 1].shape[0]) 
print("Rucni mjenjac: ", mtcars[mtcars.am == 0].shape[0]) 

#automatski mjenjac i preko 100 ks
print(mtcars[(mtcars.am == 1) & (mtcars.hp > 100)].shape[0])

#masa svakog automobila u kg
mtcars["wt"] = mtcars["wt"]*1000*0.453592
print(mtcars[["car", "wt"]])