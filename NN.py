import random
import numpy as np


def NNread():
    from mnist import MNIST
    mndata = MNIST('data')
    training_images, training_labels = mndata.load_training()
    testing_images, testing_labels = mndata.load_testing()
    return training_images, training_labels, testing_images, testing_labels


class NN():
    def __init__(self, sizes):
        self.nlayers = len(sizes)
        self.bais = [np.random.rand(x,1) for x in sizes[1:]]
        self.weights =


training_images, training_labels, testing_images, testing_labels = NNread()



# print(mndata.display(training_images[index]))
