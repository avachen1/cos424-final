#generating test and training data
import numpy as np



data = np.loadtxt('data.txt')


NUM_ROWS = data.shape[0]

training_length = np.round(NUM_ROWS * .8)


indices = np.random.choice(NUM_ROWS, training_length, replace=False)


training_data = data[indices, :]


test_data = np.delete(data, indices, 0)

np.savetxt('test_data.txt', test_data, fmt='%s')
np.savetxt('training_data.txt', training_data, fmt='%s')
