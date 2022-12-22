#!/usr/bin/env python
# coding: utf-8

# In[1]:


#upsampling
import cv2

image = cv2.imread('letter.jpg')
cv2.imshow('before', image)

image = cv2.pyrUp(image)
cv2.imshow('after', image)
cv2.waitKey()
cv2.destroyAllWindows()    


# In[29]:


#downsampling
import cv2
from matplotlib import pyplot as plt

image = cv2.imread('new.jpg')
cv2.imshow('before', image)

image = cv2.pyrDown(image)
plt.imshow(image)
cv2.imshow('after', image)
cv2.waitKey()
cv2.destroyAllWindows()    


# In[8]:


import cv2
import numpy as np

def interpolation(image, scale):

    width = int(image.shape[1] * scale / 100)
    height = int(image.shape[1] * scale / 100)
    dimensions = (width, height)

    resized = cv2.resize(image, dimensions, cv2.INTER_AREA)

    cv2.imshow('Scaled Image', resized)
    cv2.waitKey()
    cv2.destroyAllWindows()

image = cv2.imread('letter.JPG')
interpolation(image, 50)


# In[ ]:


#Up-Sampling

#nearest neighbor interpolation.
#bi-linear interpolation.
#bi-cubic interpolation


# In[21]:


import cv2
import numpy as np

img = cv2.imread('letter.jpg')
near_img = cv2.resize(img,None, fx = 5, fy = 5, interpolation = cv2.INTER_NEAREST)
cv2.imshow('Near',near_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[22]:


import cv2
import numpy as np

img = cv2.imread('letter.jpg')
bilinear_img = cv2.resize(img,None, fx = 5, fy = 5, interpolation = cv2.INTER_LINEAR)
cv2.imshow('Bilinear',bilinear_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[23]:


import cv2
import numpy as np

img = cv2.imread('letter.jpg')
bicubic_img = cv2.resize(img,None, fx = 5, fy = 5, interpolation = cv2.INTER_CUBIC)
cv2.imshow('Bicubic',bicubic_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


#Downsampling

#Plot a graph showing different types of downsampled images.



# In[30]:


#quantization

from PIL import Image 
import PIL 
im1 = Image.open("new.jpg") 
im1 = im1.quantize(26) 
im1.show() 


# In[ ]:




