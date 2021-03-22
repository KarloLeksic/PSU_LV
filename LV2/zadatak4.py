import matplotlib.pyplot as plt
import numpy as np
import skimage.io

img = skimage.io.imread('tiger.png', as_gray=True)

height = img.shape[0]
width = img.shape[1]

#povecanje brightness -> a)
p = int(100)
for i in range(0, height):
    for j in range(0, width):
        if 255 - img[i][j] <= p:
            img[i][j] = 255        
        else:
            img[i][j] += p    

#rotacija u smjeru kazaljke na satu -> b)
img2 = np.zeros((width, height), np.uint8)
for i in range(0, width):
    t = height - 1
    for j in range(0, height):
        img2[i][t] = img[j][i]
        t -= 1

#drugi nacin za rotaciju
#height, width = img.shape
#img90 = np.zeros((widht, height))
#for j in range(0, weight):q
#   img90 = [:, height - j - 1] = img[j, :]

#zrcaljenje slike(ne radi) -> c)
#for i in range(0, int(height/2)):
#    temp = img[:, i] 
#    img[:, i] = img[:, height -1- i]
#    img[:, height - i-1] = temp

# c)
img_mirr = img2 = np.zeros((height, width), np.uint8)

#smanjivanje rezolucije -> d)

plt.figure(1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()    