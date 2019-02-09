from keras.datasets import cifar10 
import numpy as np



class NearestNeighbor(object):
    def __init__(self):
        pass

    def train(self, X, y):
        """X = N x D where each row is an example. Y is 1-dimensional of size N"""
        self.Xtr = X
        self.ytr = y

    def predict(self, X):
        """X = N x D where each row is an example we wish to predict label for"""
        num_test = X.shape[0]
        Ypred = np.zeros(num_test, dtype=ytr.dtype) # lets make sure the output type matches the input type

        # loop over all test rows
        for i in range(num_test):
            # find the nearest training image to the i'th test image
            # using the L1 distance (sum of absolute value differences)
            distances = np.sum(np.abs(self.Xtr - X[i,:]), axis=1)
            min_index = np.argmin(distances) # get the index with smallest distance
            Ypred[i] = self.ytr[min_index] # predict the label of the nearest example
        return Ypred


(Xtr, ytr), (Xte, Yte) = cifar10.load_data()
Xtr_rows = Xtr.reshape(Xtr.shape[0], 32*32*3)
Xte_rows = Xte.reshape(Xte.shape[0], 32*32*3)

nn = NearestNeighbor() # create a Nearest Neighbor classifier class
nn.train(Xtr_rows, ytr) # train the classifier on the training images and labels
Yte_predict = nn.predict(Xte_rows) # predict labels on the test images
print('Accuracy: {}'.format(np.mean(Yte_predict=Yte)))

