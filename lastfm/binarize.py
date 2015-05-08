import numpy as np

train = np.genfromtxt("./training_data.txt")
test = np.genfromtxt("./test_data.txt")

binary_train = np.zeros([len(train), len(train[0])])
for i in range(len(train)):
	for j in range(len(train[0])):
		if train[i,j] > 0:
			binary_train[i,j] = 1

binary_test = np.zeros([len(test), len(test[0])])
for i in range(len(test)):
	for j in range(len(test[0])):
		if test[i,j] > 0:
			binary_test[i,j] = 1

np.savetxt('binary_train.txt', binary_train, fmt='%s')
np.savetxt('binary_test.txt', binary_test, fmt='%s')