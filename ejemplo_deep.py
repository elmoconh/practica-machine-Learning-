# -*- coding: utf-8 -*-
"""
Created on Mon May  4 23:20:55 2020

@author: Elmo
"""

import tensorflow as tf
import numpy as np
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D
from keras import backend as K

batch_size = 100
num_clases = 10 
epochs = 3
filas, columnas = 28,28

(xt, yt),(xtest,ytest) = mnist.load_data()

xt=xt.reshape(xt.shape[0],filas,columnas,1)
xtest=xtest.reshape(xtest.shape[0],filas,columnas,1)

xt= xt.astype('float32')
xtest= xtest.astype('float32')

xt = xt/255

xtest = xtest/255

yt = keras.utils.to_categorical(yt, num_clases)
ytest = keras.utils.to_categorical(ytest, num_clases)

modelo = Sequential()
modelo.add(Conv2D(64, kernel_size=(3,3), activation ='relu', input_shape=(28,28,1)))
modelo.add(Conv2D(128, kernel_size=(3,3), activation ='relu', input_shape=(28,28,1)))
modelo.add(MaxPool2D(pool_size=(2,2)))
modelo.add(Flatten())
modelo.add(Dense(68))
modelo.add(Dropout(0.25))
modelo.add(Dense(20))
modelo.add(Dropout(0.25))
modelo.add(Dense(num_clases, activation='softmax'))

modelo.compile(optimizer=keras.optimizers.Adam(), loss=keras.losses.categorical_crossentropy, metrics=['categorical_accuracy'])

modelo.fit(xt,yt, batch_size, epochs, validation_data=(xtest, ytest),verbose=2)
puntuacion = modelo.evaluate(xtest,ytest, verbose=1)
print(puntuacion)
