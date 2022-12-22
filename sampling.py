#!/usr/bin/env python
# coding: utf-8

# In[7]:


#upsampling
import cv2

image = cv2.imread('letter.jpg')
cv2.imshow('before', image)

image = cv2.pyrUp(image)
cv2.imshow('after', image)
cv2.waitKey()
cv2.destroyAllWindows()    


# In[ ]:


#downsampling
import cv2

image = cv2.imread('letter.jpg')
cv2.imshow('before', image)

image = cv2.pyrDown(image)
cv2.imshow('after', image)
cv2.waitKey()
cv2.destroyAllWindows()    


# In[ ]:




