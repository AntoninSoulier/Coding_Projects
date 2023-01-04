import tensorflow as tf
from tensorflow import keras
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense

import numpy as np
import os
import sys

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import cv2
import IPython

#from six.moves import urllib
print(tf.__version__)

(train_features, train_labels), (test_features, test_labels) = keras.datasets.boston_housing.load_data()
train_mean  = np.mean(train_features, axis=0)
train_std = np.std(train_features, axis=0)
train_features = (train_features - train_mean) / train_std

def build_model():
    model = keras.Sequential([Dense(20, activation=tf.nn.relu, input_shape=[len(train_features[0])]),Dense(1)])
    model.compile(optimizer = tf.optimizers.Adam(), loss='mse', metrics=['mae','mse'])
    return model

class PrintDot(keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs):
        if epoch%100==0: print('')
        print('.', end='')

model = build_model()
early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=50)
history = model.fit(train_features, train_labels, epochs=1000, verbose = 0, validation_split=0.1, callbacks=[early_stop,PrintDot()])
hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch

rmse_final = np.sqrt(float(hist['val_mae'].tail(1)))
print()
print('Final Root Mean Square Error on validation set {}'.format(round(rmse_final,3)))

def plot_history():
    plt.figure()
    plt.xlabel('Epoch')
    plt.ylabel("Mean Square Error")
    plt.plot(hist['epoch'], hist['val_mse'], label='Val Error')
    plt.plot(hist['epoch'], hist['val_mae'], label='Val Error')
    plt.legend()
    plt.ylim([0,50])

plot_history()