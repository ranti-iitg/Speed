import cv2
import numpy as np


from keras.models import load_model
model = load_model('')

f=open('test.txt','w')
for i in xrange(1,10796):
		imlist=[]
		fname0="frame"+str(i-1)+".jpg"
		fname1="frame"+str(i)+".jpg"
		print fname1
		im0=cv2.imread("./data3/"+fname0)
		im1=cv2.imread("./data3/"+fname1)
		if im1!=None and im0!=None:
			res0=cv2.resize(im0,(200,200))
			res1=cv2.resize(im1,(200,200))
			imlist.append(res1-res0)
			imlistnp=np.array(imlist,dtype='float')
			#imlistnp=np.expand_dims(imlistnp,axis=0)
			pp=model.predict(imlistnp)
			print pp[0][0]
			if pp[0][0]<0.0:
				f.write('0.0')
				f.write('\n')
			else:
				f.write(str(pp[0][0]))
				f.write('\n')
		else:
			print "eeeeeeeeeeeeeeeeeee"
