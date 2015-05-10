# import numpy as np
# import csv
# import operator
# from sklearn import mixture
# from sklearn import cluster

# total_users = []
# total_artists = []
# total_freqs = []
# f=open('./lastfm-dataset-360K/usersha1-artmbid-artname-plays.tsv')
# for i in range(500000):
# 	line=f.next().split('\t')
# 	total_users.append(line[0])
# 	total_artists.append(line[2])
# 	total_freqs.append(line[3])

# print "raw data loaded"

# users_1k = []
# artists_1k = []
# freqs_1k = []
# count = 0
# for i in range(len(total_users)):
# 	users_1k.append(total_users[i])
# 	artists_1k.append(total_artists[i])
# 	freqs_1k.append(total_freqs[i])
# 	if total_users[i] != total_users[i-1]:
# 		count += 1
# 	if count == 10000:
# 		break

# print "created 1k data"

# # put users in dict: key=user, val=index

# users = {}
# user_count = 0

# for i in range(len(users_1k)):
# 	if users_1k[i] not in users:
# 		users[users_1k[i]] = user_count
# 		user_count += 1

# print "user_count:", user_count

# # get top 1000 artists by number of users

# NUM_ARTISTS = 1000

# artists = {}

# for i in range(len(users_1k)):
#  	if artists_1k[i] not in artists:
#  		artists[artists_1k[i]] = 1
#  	else:
#  		artists[artists_1k[i]] += 1

# sorted_artists = sorted(artists.items(), key=operator.itemgetter(1), reverse=True)

# new_artists = []

# for i in range(NUM_ARTISTS):
#  	new_artists.append(sorted_artists[i][0])

# artists = {}
# artist_count = 0

# for i in range(len(new_artists)):
# 	if new_artists[i] not in artists:
# 		artists[new_artists[i]] = artist_count
# 		artist_count += 1

# print "artist_count:", artist_count


# # fill in matrix (user_count x artist_count) with frequencies

# matrix = np.zeros([user_count, artist_count])
# for i in range(len(users_1k)):
# 	if (artists_1k[i] in artists):
# 		matrix[users[users_1k[i]]][artists[artists_1k[i]]] = freqs_1k[i]

# print "matrix created"

# counts = []
# for i in range(0,100):
# 	counts.append(0)

# delete = []
# for i in range(user_count):
# 	count = 0
# 	for j in range(artist_count):
# 		if (matrix[i,j] != 0):
# 			count += 1
# 	if (count < 2):
# 		delete.append(i)

# new_matrix = np.delete(matrix,delete,0)

# print "pruned matrix created"

data = np.genfromtxt("./data.txt")

g = mixture.GMM(n_components = 10)
g.fit(new_matrix)

print "gmm fit"

print ""

means = g.means_
weights = g.weights_
comp_row = np.zeros([means.shape[1],2])
for i in range(0,means.shape[0]):
	print weights[i]
	for j in range(0,means.shape[1]):
		comp_row[j][0] = means[i][j]
		comp_row[j][1] = j
	sorted_row = np.lexsort((comp_row[:,1],comp_row[:,0]))
	sorted_values = np.sort(comp_row[:,0])
	reversed_sorted = sorted_values[::-1]
	for j in range(10):
		for key in artists:
			if (artists.get(key) == sorted_row[j]):
				print key,
				print reversed_sorted[j]
	print ""


km = cluster.KMeans(n_clusters = 10)
km.fit(new_matrix)

print "kmeans fit"

print ""

centers = km.cluster_centers_
comp_row = np.zeros([centers.shape[1],2])
for i in range(0,centers.shape[0]):
	for j in range(0,centers.shape[1]):
		comp_row[j][0] = centers[i][j]
		comp_row[j][1] = j
	sorted_row = np.lexsort((comp_row[:,1],comp_row[:,0]))
	sorted_values = np.sort(comp_row[:,0])
	reversed_sorted = sorted_values[::-1]
	for j in range(10):
		for key in artists:
			if (artists.get(key) == sorted_row[j]):
				print key,
				print reversed_sorted[j]
	print ""












