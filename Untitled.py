#!/usr/bin/env python
# coding: utf-8

# In[12]:


#spatial filters averaging filter and median filter and median filter in image processing
import cv2
import numpy as np


# In[16]:


img_noisy1=cv2.imread("C:/Users/User/Downloads/noisy.jfif",0)


# In[14]:


#obtaining the number of rows and columns
m,n=img_noisy1.shape


# In[18]:


#traverse the image for every 3x3 area and find the median of the pixel and replace the center pixel
img_new1=np.zeros([m,n])
for i in range(1,m-1):
    for j in range(1,n-1):
        temp=[img_noisy1[i-1,j-1],img_noisy1[i-1,j],img_noisy1[i-1,j+1],img_noisy1[i,j-1],img_noisy1[i,j],img_noisy1[i,j+1],img_noisy1[i+1,j-1],img_noisy1[i+1,j],img_noisy1[i+1,j+1]]
        temp=sorted(temp)
        img_new1[i,j]=temp[4]
        img_new1=img_new1.astype(np.uint8)
cv2.imshow("median filterd image",img_new1)
cv2.waitKey()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:




