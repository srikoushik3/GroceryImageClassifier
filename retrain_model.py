# Basic Libraries
import os
import numpy as np
import math
from argparse import ArgumentParser

# Graphing
import matplotlib.pyplot as plt

# Data and image preprecessing Libraries
import scipy.misc

# ML Libraries for neural nets
from keras.applications.inception_v3 import InceptionV3
from keras.preprocessing import image
from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D
from keras import backend as K

# local libary to get preprocessed data
from preprocess import *

# create the base pre-trained model
base_model = InceptionV3(weights='imagenet', include_top=False)

# add a global spatial average pooling layer
x = base_model.output
'''
x = GlobalAveragePooling2D()(x)
# let's add a fully-connected layer
x = Dense(1024, activation='relu')(x)
'''
# and a logistic layer with 25 classes (25 grocery products)
predictions = Dense(25, activation='softmax')(x)

# model to train
model = Model(inputs=base_model.input, outputs=predictions)

'''
# visualize the layers of the InceptionV3 model to know which ones to freeze
for i, layer in enumerate(base_model.layers):
   print(i, layer.name)
'''

# train the top 1 inception layer, i.e. freeze
# the first 310 layers and unfreeze the rest:
for layer in model.layers[:310]:
   layer.trainable = False
for layer in model.layers[310:]:
   layer.trainable = True

# compile the model for these modifications to take effect
from keras.optimizers import SGD
model.compile(optimizer=SGD(lr=0.0001, momentum=0.9), loss='categorical_crossentropy')

# train the model using the load_images batch generator
history = model.fit_generator(load_images(TRAIN_PATH), steps_per_epoch=10, epochs=1)

# list all data in history
print(history.history.keys())

# summarize history for accuracy
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
