from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers import Dense,Activation
from keras.models import Sequential

model=Sequential()
model.add(Convolution2D(10, 3, 3, border_mode='same',input_shape=(200,200,3)))
model.add(Activation('relu'))
model.add(Convolution2D(10, 3, 3,border_mode='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Convolution2D(10, 3, 3, border_mode='same'))
model.add(Activation('relu'))
model.add(Convolution2D(10, 3, 3,border_mode='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='linear'))
model.compile(loss='mse',optimizer='adam',metrics=['mse'])

h = model.fit(X,Y, verbose=1, validation_split=0.1, nb_epoch=40,shuffle=True)