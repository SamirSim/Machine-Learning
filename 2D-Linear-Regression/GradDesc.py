import scipy.misc as sc
import numpy as np
import matplotlib.pyplot as plt

def nomalize(inputs):
    list = (inputs - inputs.mean()) / inputs.std()
    return list

def J(X, Y, theta):
    return (len(Y) / 2) * np.sum(np.power((X[:,1] * theta[1] + theta[0]) - Y, 2)) 

def minFunction(X, Y, theta, maxIters, alpha):
    iters = 0
    costs = []
    while  iters < maxIters:
        saveTheta0 = theta[0]
        saveTheta1 = theta[1]
        theta[1] = saveTheta1 - (alpha / len(Y)) * np.sum(((saveTheta0 + (saveTheta1 * X[:,1])) - Y) * X[:,1])
        theta[0] = saveTheta0 - (alpha / len(Y)) * np.sum(((saveTheta0 + (saveTheta1 * X[:,1])) - Y) * X[:,0])
        costs.append(J(X, Y, theta))
        iters = iters + 1
    return theta, costs