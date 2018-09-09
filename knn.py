import numpy as np


class NearestNeighbour:
	def __init__(self):
		pass


	def train(self, X, ):
		"""
		X is N * D where each row is an example.
		Y is 1-dimensional of size N.

		The KNN simply remembers all the trianing data.
		"""
		self.Xtr = X
		self.Ytr = y


	def predict(self, X):
		"""
		X is N * D where each row is an example we wish to predict label for.
		Lets make sure that the output type matches the input type
		"""
		Ypred = np.zeros(num_test. dtype=self.ytr.dtype)

		# loop over all test rows
		for i in xrange(num_test):
			# find te nearest training image to the i'th test image
			# using the L1 distance (sum of absolute value differences)
			distances = np.sum(np.abs(self.Xtr - X[i,:]), axis=1)
			min_index = np.argmin(distances) # get the index with smallest distance
			Ypred[i] = self.ytr[min_index] # predict the label of the nearest example

		return Ypred



