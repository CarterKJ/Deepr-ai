from deeprai import models
from Datasets.MNIST import mnist as db
import numpy as np
inputs = db.load_x(3000)
expected = db.load_y(3000)

test_x = db.load_x(10000)
test_y = db.load_y(10000)

network = models.FeedForward()
network.add_dense(784)

network.add_dense(60, activation='tanh')
network.add_dense(10, activation='sigmoid')

network.train_model(input_data=inputs, verify_data=expected, test_input=test_x,test_targets=test_y, batch_size=136,
                    epochs=1000, learning_rate=6.6)
