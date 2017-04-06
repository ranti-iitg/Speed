from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np
from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D
from keras.callbacks import TensorBoard
from random import randint


base_model = ResNet50(weights='imagenet', include_top=False)
b = base_model.output
b = GlobalAveragePooling2D()(b)
b = Dense(1024, activation='relu')(b)
predictions = Dense(1, activation='linear')(b)

model = Model(input=base_model.input, output=predictions)
model.compile(loss='mse',optimizer='adam',metrics=['mse'])


h = model.fit(imX,imY, verbose=1, batch_size=16,validation_split=0.1, nb_epoch=25,shuffle=True)