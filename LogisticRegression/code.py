def sigmoid(x):
    return (1/(1 + np.exp(-x)))

def h(x, theta):
    return sigmoid(np.dot(x, theta))

# Loss function to minimize
def J(x,y,theta): 
    hxi = 1 / (1 + np.exp(-(theta[0] + theta[1] * X[:,0] + theta[2] * X[:,1])))
    var = (y) * np.log (hxi) + (1 - y) * np.log (1 - hxi)
    return (- 1 / m) * (np.sum(var))

# Training function of the model using Gradient Descents
def train(x,y, theta ): 
    iters = 0
    maxIters = 1000
    continu = True
    while continu and iters < maxIters:
        cost = J(x, y, theta)
        hxi = 1 / (1 + np.exp(-(theta[0] + theta[1] * X[:,0] + theta[2] * X[:,1])))
        saveTheta = theta.copy()
        theta[0] = saveTheta[0] - (learning_rate / m) * np.sum(hxi - y)   
        theta[1] = saveTheta[1] - (learning_rate / m) * np.sum((hxi - y) * x[:,0])       
        theta[2] = saveTheta[2] - (learning_rate / m) * np.sum((hxi - y) * x[:,1])
        if J(x, y, theta) > cost:
            continu = False
        iters = iters + 1
    return theta  

# Train the model
train(X_norm,Y,theta)

