from random import randint
import numpy as np

class Cluster:
    def __init__(self,mean,v):
        self.mean = []
        self.mean = mean
        self.elements = []
        self.elements.append((v))
    
    def addElement(self,v):
        self.elements.append(v)

    def removeElement(self, v):
        self.elements.remove(v)

def distance(a,b):
    return np.sum(np.power((np.array(a) - b), 2))

def initCenters(dataSet, nbClasses):#Initialisation centres
    clusters = []
    for _ in range(0,nbClasses): 
        c = dataSet[randint(0,len(dataSet)-1)]
        clusters.append(Cluster(c,c))
    return clusters

def RAZ(n):
    v = []
    for _ in range(0,n):
        v.append(0)
    return v
    
def kmeans(dataSet, dim, nbClasses):#CLassification
    clusters = initCenters(dataSet,nbClasses)
    var = []
    var = RAZ(dim)
    stop = False
    while stop == False:
        stop = True
        for i in dataSet: 
            tempDis = distance(i,clusters[0].mean)
            tempCluster = 0
            for j in range(0,nbClasses):
                if distance(i,clusters[j].mean) < tempDis:
                    tempDis = distance(i,clusters[j].mean)
                    tempCluster = j
            temp = clusters[tempCluster].elements
            if tuple(i) not in list(map(tuple, temp)):
                stop = False
                for j in range(0,nbClasses):
                    if tuple(i) in list(map(tuple,clusters[j].elements)):
                        print(len(clusters[j].elements)," **** ",i," ****** ",clusters[j].elements[0])
                        print (np.delete(clusters[j].elements,i));
                        #np.delete(clusters[j].elements,i);
                        clusters[j].removeElement
                        #list(map(tuple,clusters[j].elements)).remove(tuple(i))
                        print(len(clusters[j].elements)," *** ",clusters[j].elements)
                clusters[tempCluster].addElement(i)
        for j in range(0,nbClasses):
            for i in clusters[j].elements:
                var = np.sum([i, var], axis = 0)
            clusters[j].mean = []
            clusters[j].mean = var / len(clusters[j].elements)
            var = RAZ(dim)
    return clusters