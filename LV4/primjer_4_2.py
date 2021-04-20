import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

def non_func(x):
    y = 1.6345 - 0.6235*np.cos(0.6067*x) - 1.3501*np.sin(0.6067*x) - 1.1622 * np.cos(2*x*0.6067) - 0.9443*np.sin(2*x*0.6067)
    return y

def add_noise(y):
    np.random.seed(14)
    varNoise = np.max(y) - np.min(y)
    y_noisy = y + 0.1*varNoise*np.random.normal(0,1,len(y))
    return y_noisy
 
x = np.linspace(1,10,50)
y_true = non_func(x)
y_measured = add_noise(y_true)

x = x[:, np.newaxis]
y_measured = y_measured[:, np.newaxis]

# make polynomial features
poly2 = PolynomialFeatures(degree=2)
poly6 = PolynomialFeatures(degree=6)
poly = PolynomialFeatures(degree=15)
xnew2 = poly2.fit_transform(x)
xnew6 = poly6.fit_transform(x)
xnew = poly.fit_transform(x)
    
np.random.seed(12)
indeksi = np.random.permutation(len(xnew))
indeksi_train = indeksi[0:int(np.floor(0.7*len(xnew)))]
indeksi_test = indeksi[int(np.floor(0.7*len(xnew)))+1:len(xnew)]

xtrain = xnew[indeksi_train,]
ytrain = y_measured[indeksi_train]
xtrain2 = xnew2[indeksi_train,]
ytrain2 = y_measured[indeksi_train]
xtrain6 = xnew6[indeksi_train,]
ytrain6 = y_measured[indeksi_train]

xtest = xnew[indeksi_test,]
ytest = y_measured[indeksi_test]
xtest2 = xnew2[indeksi_test,]
ytest2 = y_measured[indeksi_test]
xtest6 = xnew6[indeksi_test,]
ytest6 = y_measured[indeksi_test]

linearModel = lm.LinearRegression()
linearModel.fit(xtrain,ytrain)
linearModel2 = lm.LinearRegression()
linearModel2.fit(xtrain2,ytrain2)
linearModel6 = lm.LinearRegression()
linearModel6.fit(xtrain6,ytrain6)

ytest_p = linearModel.predict(xtest)
MSE_test = mean_squared_error(ytest, ytest_p)
ytest_p2 = linearModel2.predict(xtest2)
MSE_test2 = mean_squared_error(ytest2, ytest_p2)
ytest_p6 = linearModel6.predict(xtest6)
MSE_test6 = mean_squared_error(ytest6, ytest_p6)

print("MSE 2 deg: ", MSE_test2)
print("MSE 6 deg: ", MSE_test6)
print("MSE 15 deg: ", MSE_test)

plt.figure(1)
plt.plot(xtest[:,1],ytest_p,'og',label='predicted')
plt.plot(xtest[:,1],ytest,'or',label='test')
plt.legend(loc = 4)
plt.show()

plt.figure(2)
plt.plot(xtest2[:,1],ytest_p2,'og',label='predicted')
plt.plot(xtest2[:,1],ytest2,'or',label='test')
plt.legend(loc = 4)
plt.show()

plt.figure(3)
plt.plot(xtest6[:,1],ytest_p6,'og',label='predicted')
plt.plot(xtest6[:,1],ytest6,'or',label='test')
plt.legend(loc = 4)
plt.show()

#pozadinska funkcija vs model
plt.figure(4)
plt.plot(x,y_true,label='f')
plt.plot(x, linearModel.predict(xnew),'r-',label='model 15 deg')
plt.plot(x, linearModel2.predict(xnew2),'g-',label='model 2 deg')
plt.plot(x, linearModel6.predict(xnew6),'b-',label='model 6 deg')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(xtrain[:,1],ytrain,'ok',label='train')
plt.legend(loc = 4)
plt.show()