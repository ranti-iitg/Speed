from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np
from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D
from keras.callbacks import TensorBoard
from random import randint


base_model = VGG16(weights='imagenet', include_top=False)
b = base_model.output
b = GlobalAveragePooling2D()(b)
b = Dense(1024, activation='relu')(b)
predictions = Dense(1, activation='linear')(b)

model = Model(input=base_model.input, output=predictions)
model.compile(loss='mse',optimizer='adam',metrics=['mse'])



from keras.preprocessing.image import ImageDataGenerator

datagen=ImageDataGenerator()

from keras.models import load_model
model = load_model('dif_1_4000.m5')

x_val=X[1900:]
y_val=Y[1900:]
from random import randint
for i in range(10):
	print i
	k=randint(0,1400)
	xx=X[k:k+500]
	yy=Y[k:k+500]
	model.fit(xx,yy,nb_epoch=1,shuffle=True,validation_split=0.1,verbose=0)

h = model.fit(imX,imY, verbose=1, batch_size=16,validation_split=0.1, nb_epoch=100,shuffle=True)



all_images1=np.load('im1.npz')
x=all_images1['img1']

x = preprocess_input(x)
