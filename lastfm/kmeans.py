from scipy import sparse
import numpy as np
from sklearn.decomposition import TruncatedSVD, RandomizedPCA, NMF
from sklearn.metrics import precision_recall_curve, auc
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from functools import partial
import math
from lda import LDA

def nmf(X):
  name = "nmf"
  if binary:
    name = "binary_"  + name
  print name
  model = NMF(n_components = 25)
  model.fit(X)
  A_T = sparse.csc_matrix(model.components_)
  Z = A_T*X
  A = A_T.transpose()
  def get_prob(i, j):
    return (A.getrow(i)*Z.getcol(j))[0,0]
  display_results(name, get_prob) 

def kmeans(X, n_clusters):
	name = "kmeans" + str(n_clusters)
	if binary:
		name = "binary_"  + name
	print name
	model = KMeans(n_clusters = 50)
	labels = model.fit_predict(X)
	def get_prob(i,j):
		return model.cluster_centers_[labels[i]][j]
	display_results(name, get_prob)

def display_results(name, get_prob):
	f_test = open('testTriplets.txt', 'r')
	f_out = open(name+"Probs.txt", "w")
	test = np.array([l.split() for l in f_test.readlines()])
	probs = []
	trues = [] 
	for l in test: 
		i = int(l[0])
		j = int(l[1])
		value = int(l[2])

		prob = get_prob(i,j)
		if prob > 1 :
			prob = 1
		elif prob < 0:
			prob = 0
		f_out.write(str(prob)+"\n")
		trues.append(value)
		probs.append(prob)
	f_test.close()
	f_out.close()

binaries = [True, False]
for binary in binaries:
	if binary:
		train = np.genfromtxt("./binary_train.txt")
		test = np.genfromtxt("./binary_test.txt")		
	else:
		train = np.genfromtxt("./train.txt")
		test = np.genfromtxt("./test.txt")

	svd(X)
	kmeans(X, 25)
	if not binary:
		lda(X, 25)
	nmf(X)

plt.legend()
plt.show()

