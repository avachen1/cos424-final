import numpy as np
import scipy as sci

data = np.genfromtxt('/Users/nabeelsarwar/Documents/PrincetonJuniorSpring/COS424/HW/FinalProjectGit/cos424-final/lastfm/train.txt')

NUM_VARIABLES = data.shape[1]

#K clusters
K = 20

clusterMean = []

multinomial = np.zeros(K)

for i in range(K):
    multinomial[i] = 1.0/K


#initialize clusters randomly
for i in range(K):
    mean = np.zeros(NUM_VARIABLES)
    for j in range(NUM_VARIABLES):
        mean[j] = np.random.randint(0, high=100)
    
    clusterMean.append(mean)

print 'Created Means'

#this is a matrix of the condition probabilities
#number of samples by number of clusters
conditionals = np.empty((data.shape[0], K))

print 'Created Conditionals'

def PoissonProbability(value, mean):
    return mean ** value * np.exp(-mean) / sci.misc.factorial(value)

PoissonProbability = np.vectorize(PoissonProbability)

def updateConditions():
    for i in range(conditionals.shape[0]):
        rowsumForBayes = 0
        for j in range(conditionals.shape[1]):
            rowsumForBayes = rowsumForBayes + multinomial[j] * np.prod(PoissonProbability(data[i,:], clusterMean[j]))
        for j in range(conditionals.shape[1]):
            conditionals[i, j] = multinomial[j] * np.prod(PoissonProbability(data[i,:], clusterMean[j])) / rowsumForBayes


def updateMultiNomial():
    for i in range(multinomial.shape[0]):
        multinomial[i] = np.sum(conditionals[:, i])/data.shape[0]

def updateMeans():
    for i in range(len(clusterMean)):
        numerator = 0 
        for j in range(len(conditionals.shape[0])):
            #you want j, i for real in here as in the notation of the book
            
            numerator = conditionals[j, i] * data[i, :]
        if (numerator.shape[0] != clusterMean[i].shape[0]):
            print 'Size mismatch'
        clusterMean[i] = numerator/(multinomial[i] * data.shape[0])


updateConditions()
updateMultiNomial()
updateMeans()

