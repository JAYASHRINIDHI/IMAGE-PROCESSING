#!/usr/bin/env python
# coding: utf-8

# In[1]:


#bitwise operator
import cv2 
img1=cv2.imread("sky.jfif")
img2=cv2.imread("moon.jfif")

bitwise_AND=cv2.bitwise_and(img1,img2)
bitwise_OR=cv2.bitwise_or(img1,img2)
bitwise_NOT=cv2.bitwise_not(img1)

cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.imshow("AND",bitwise_AND)
cv2.imshow("OR",bitwise_OR)
cv2.imshow("NOT",bitwise_NOT)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[11]:


#changing the background of an image
from PIL import Image,ImageDraw,ImageFilter
im1=Image.open("aaa.jpg")
im2=Image.open("bhoomi.jpg")
mask_im=Image.new("L",im2.size,0)
draw=ImageDraw.Draw(mask_im)
draw.ellipse((150,105,410,300),fill=225)
mask_im_blur=mask_im.filter(ImageFilter.GaussianBlur(10))
back_im=im1.copy()
back_im.paste(im2,(0,0),mask_im_blur)
back_im.show()


# In[ ]:





# In[ ]:




