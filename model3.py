from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np
from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D
from keras.callbacks import TensorBoard
from random import randint
from keras.layers import Convolution2D
from keras.layers import Embedding, Input, merge
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers import Dense,Activation

base_model2 = VGG16(weights='imagenet', include_top=False)
b2 = base_model2.output
base_model1 = VGG16(weights='imagenet', include_top=False)
b1 = base_model2.output
M = merge([b2,b1], mode='concat', concat_axis=1)
pp=Convolution2D(10, 3, 3, border_mode='same')(M)
pp= GlobalAveragePooling2D()(pp)
pp=Dense(512)(pp)
pp=Activation('relu')(pp)
pp=Dropout(0.5)(pp)
pp=Dense(1, activation='linear')(pp)
model = Model(input=[base_model2.input, base_model1.input], output=[pp])
model.compile(loss='mse',optimizer='adam',metrics=['mse'])

h = model.fit([X1, X0],Y,batch_size = 4, nb_epoch=10, verbose=1,validation_split=0.1, shuffle=True)
