#!/usr/bin/env python
# coding: utf-8

# In[3]:


#video to frame
import cv2
vid = cv2.VideoCapture("videoplayback.mp4") 
i=0
while(True):  
    ret, frame = vid.read()  
    cv2.imshow('frame', frame) 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
    cv2.imwrite('bhanu'+str(i)+'.jpg',frame)
    i+=1
    
vid.release() 
cv2.destroyAllWindows() 


# In[7]:


import cv2
import numpy as np 

cap = cv2.VideoCapture('videoplayback.mp4')


while True:
    _, frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) == 27:
        break



cap.release()
cv2.destroyAllWindows()


# In[23]:


#box filter blur

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('nature.jpg')

blur = cv2.blur(img,(5,5))

cv2.imshow("original",img)
cv2.imshow("box filter",blur)

cv2.waitKey(0)
cv2.destroyAllWindows() 


# In[24]:


#shading correction

import cv2

img = cv2.imread('ChessBoardGrad.png')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image', grayImg)
cv2.waitKey(0)

filtersize = 513
gaussianImg = cv2.GaussianBlur(grayImg, (filtersize, filtersize), 128)
cv2.imshow('Converted Image', gaussianImg)
cv2.waitKey(0)

newImg = (grayImg-gaussianImg)
cv2.imshow('New Image', newImg)
cv2.imwrite('Converted.png', newImg)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




