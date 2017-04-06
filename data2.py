import cv2
import numpy as np
vidcap = cv2.VideoCapture('./data/train.mp4')
success,image = vidcap.read()
count = 0
success = True
while success:
  success,image = vidcap.read()
  print 'Read a new frame: ', success
  cv2.imwrite("./data2/frame%d.jpg" % count, image)     # save frame as JPEG file
  count += 1

import cv2
import numpy as np
imlist_small_diff1=[]
imlist_small_diff0=[]
for i in xrange(20000):
	
	if i%20==1:
		fname0="frame"+str(i-1)+".jpg"
		fname1="frame"+str(i)+".jpg"
		print fname1
		im0=cv2.imread("./data2/"+fname0)
		im1=cv2.imread("./data2/"+fname1)
		if im1!=None and im0!=None:
			res0=cv2.resize(im0,(200,200))

			res1=cv2.resize(im1,(200,200))


			imlist_small_diff1.append(res1)
			imlist_small_diff0.append(res0)
		else:
			print "eeeeeeeeeeeeeeeeeee"


imlist_small_diff1=np.array(imlist_small_diff1,dtype='float')
imlist_small_diff0=np.array(imlist_small_diff0,dtype='float')

np.savez('imlist_2_small_diff_1000.npz',imlist_small_diff_0_1000=imlist_small_diff0,imlist_small_diff_1_1000=imlist_small_diff1)

f = open("./data/train.txt")
content=f.readlines()
content_list=[float(x) for x in content]
content_list=np.array(content_list)
ylist_small_diff=[]
for i in xrange(20000):
	if i%20==1:
		ylist_small_diff.append(content_list[i])

ylist_small_diff=np.array(ylist_small_diff)
np.savez('ylist_2_small_diff_1000.npz',ylist_2_small_diff_1000=ylist_small_diff)

import numpy as np
from sklearn.utils import shuffle
imgs=np.load("imlist_2_small_diff_1000.npz")
yy=np.load("ylist_2_small_diff_1000.npz")
imX0=imgs['imlist_small_diff_0_1000']
imX1=imgs['imlist_small_diff_1_1000']
imY=yy['ylist_2_small_diff_1000']
X0,X1,Y=shuffle(imX0,imX1,imY)



np.savez('im4.npz',img4=imlist4)