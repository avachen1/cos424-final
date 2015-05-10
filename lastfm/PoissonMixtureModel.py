import numpy as np
import scipy as sci
import scipy.misc as scimisc
from scipy.special import gammaln

data = np.genfromtxt('/Users/nabeelsarwar/Documents/PrincetonJuniorSpring/COS424/HW/FinalProjectGit/cos424-final/lastfm/train.txt')

NUM_VARIABLES = data.shape[1]

#K clusters
K = 10

clusterMean = []

multinomial = np.zeros(K)

for i in range(K):
    multinomial[i] = 1.0/K

print multinomial
#initialize clusters randomly
for i in range(K):
    mean = np.zeros(NUM_VARIABLES)
    for j in range(NUM_VARIABLES):
        mean[j] = np.random.randint(10, high=300)
    
    clusterMean.append(mean)

print 'Created Means'

#this is a matrix of the condition probabilities
#number of samples by number of clusters
conditionals = np.empty((data.shape[0], K))

print 'Created Conditionals'

def PoissonProbability(value, mean):
    if value==0:
        return np.exp(-mean)
    return value * np.log(mean) - mean - gammaln(value)

def PoissonProbabilityVector(vector, mean):
    values = np.zeros(vector.shape[0])
    for i in range(vector.shape[0]):
        values[i] = PoissonProbability(vector[i], mean[i])
    return values
    
def updateConditions():
    for i in range(conditionals.shape[0]):
        rowsumForBayes = np.zeros(K)
        for j in range(conditionals.shape[1]):
            if (data[i, :].shape[0] != clusterMean[j].shape[0]):
                print 'size mismatch 1'
            rowsumForBayes[j] = np.log(multinomial[j]) + np.sum(PoissonProbabilityVector(data[i, :], clusterMean[j]))
        rowsumForBayes = scimisc.logsumexp(rowsumForBayes)  
        for j in range(conditionals.shape[1]):
            conditionals[i, j] = np.exp(np.log(multinomial[j]) + np.sum(PoissonProbabilityVector(data[i,:], clusterMean[j])) - rowsumForBayes)
        if (i % 10 == 0):
            print 'Finished Conditions for {0}:'.format(i)



def updateMultiNomial():
    for i in range(multinomial.shape[0]):
        multinomial[i] = np.sum(conditionals[:, i])/data.shape[0]
        print 'Finished Multinomial for {0}:'.format(i)

def updateMeans():
    for i in range(len(clusterMean)):
        numerator = 0 
        for j in range(conditionals.shape[0]):
            #you want j, i for real in here as in the notation of the book
            numerator = numerator + conditionals[j, i] * data[j, :]
        if (numerator.shape[0] != clusterMean[i].shape[0]):
            print 'Size mismatch 2 '
        clusterMean[i] = numerator/(multinomial[i] * data.shape[0])
        print 'Finished means for {0}:'.format(i)


updateConditions()
updateMultiNomial()
updateMeans()

for i in range(20):
    updateConditions()
    updateMultiNomial()
    updateMeans()

#now we need to output the max conditional for each row
whichGroupMax = np.zeros(data.shape[0])

whichGroupMax = np.argmax(conditional, axis = 0)

np.savetxt('clustersOfTrainData.txt', whichGroupMax, fmt='%s')


#what does each cluster have
clusterIndices = []
for i in range(len(clusterMean)):
    clusterIndices.append(np.argsort(clusterMean[i])[-5:])
    



