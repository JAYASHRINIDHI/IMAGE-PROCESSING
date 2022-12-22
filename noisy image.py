#!/usr/bin/env python
# coding: utf-8

# In[2]:


#spatial filters averaging filter and median filter and median filter in image processing
import cv2
import numpy as np


# In[3]:


img_noisy1=cv2.imread("C:/Users/User/Downloads/noisy.jfif",0)


# In[4]:


#obtaining the number of rows and columns
m,n=img_noisy1.shape


# In[5]:


#traverse the image for every 3x3 area and find the median of the pixel and replace the center pixel
img_new1=np.zeros([m,n])
for i in range(1,m-1):
    for j in range(1,n-1):
        temp=[img_noisy1[i-1,j-1],img_noisy1[i-1,j],img_noisy1[i-1,j+1],
              img_noisy1[i,j-1],img_noisy1[i,j],img_noisy1[i,j+1],
              img_noisy1[i+1,j-1],img_noisy1[i+1,j],img_noisy1[i+1,j+1]]
        temp=sorted(temp)
        img_new1[i,j]=temp[4]
        img_new1=img_new1.astype(np.uint8)
cv2.imshow("median filterd image",img_new1)
cv2.waitKey()
cv2.destroyAllWindows()


# In[12]:


#low pass spatial domain filtering to observe the blurring effect
import cv2
import numpy as np
img=cv2.imread("C:/Users/User/Downloads/noisy.jfif",0)
m,n=img.shape
#develop averaging filter(3,3) mask
mask=np.ones([3,3],dtype=int)
mask=mask/9
#construct 3x3 mask over theimage
img_new=np.zeros([m,n])
for i in range(1,m-1):
    for j in range(1,n-1):
        temp=img[i-1,j-1]*mask[0,0]+img[i-1,j]*mask[0,1]+img[i-1,j+1]*mask[0,2]+img[i,j-1]*mask[1,0]+img[i,j]*mask[1,1]+img[i,j+1]*mask[1,2] +img[i+1,j-1]*mask[2,0]+img[i+1,j]*mask[2,1]+img[i+1,j+1]*mask[2,2]
        img_new[i,j]=temp
        img_new=img_new.astype(np.uint8)
cv2.imshow("median filterd image",img_new)
cv2.waitKey()
cv2.destroyAllWindows()            


# In[ ]:





# In[ ]:




