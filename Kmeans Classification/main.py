from random import randint
import Kmeans as km
import pandas as pd
import matplotlib.pyplot as plt 
import csv

def loadData():
    data = pd.DataFrame(pd.read_csv("dataset.txt",names=range(0,5)))
    return data.loc[:,0:1].values

dataSet = loadData()
nbClasses = 3
dim = len(dataSet[0])

clusters = km.kmeans(dataSet, dim, nbClasses)
print(len(clusters[0].elements)+len(clusters[1].elements)+len(clusters[2].elements))

number = 0 
colors = ["r","b","g","black"] 
for cl in clusters :
    plt.scatter(list(map(lambda x:x[0], cl.elements)),list(map(lambda x:x[1], cl.elements)),c = colors[number])
    plt.scatter(cl.mean[0], cl.mean[1], c = colors[number], marker = "+")
    number = number + 1
plt.show()

