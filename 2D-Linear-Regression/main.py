import GradDesc as grd
import pandas as pd
import numpy as np
from random import randint
import matplotlib.pyplot as plt

#Initializing parameters
alpha = 0.01
maxIters = 500
theta = [randint(0, 1000),randint(0, 1000)]

#Part One 
header = ["Superficie", "Prix"]
houses = pd.read_csv("datasets/houses.csv", names=header)

X = houses.iloc[:,:-1].values 
Y = houses.iloc[:,-1].values 

X = grd.nomalize(X)
ones = np.ones([X.shape[0],1])
X = np.concatenate((ones,X),axis=1)
list, costs = grd.minFunction(X, Y, theta, maxIters, alpha)

plt.scatter(X[:,1], Y)
plt.xlabel('Superficie')
plt.ylabel('Prix')
plt.show()

plt.scatter(X[:,1], Y)
plt.plot(X[:,1], list[0] + list[1] * X[:,1])
plt.show()
plt.plot(costs)
plt.show()

#Part Two 
header= [ "Latitude", "Mortality", "Ocean", "Long"]
skinCancer = pd.read_csv("datasets/skincancer.txt",  names=header)
skinCancer.head()

plt.scatter(skinCancer.iloc[:,0], skinCancer.iloc[:,1])
plt.xlabel('Latitude')
plt.ylabel('Mortality')
plt.show()

X = skinCancer.iloc[:,:1].values
Y = skinCancer.iloc[:,1].values
X = grd.nomalize(X)

ones = np.ones([len(X),1])
X = np.concatenate((ones,X),axis=1)
theta = np.random.rand(X.shape[1])

X = grd.nomalize(X)
list, costs = grd.minFunction(X, Y, theta, maxIters, alpha)
plt.scatter(X[:,1], Y)
plt.plot(X[:,1], theta[0] + theta[1] * X[:,1])
plt.show()
print(list[-1])
print(theta)
