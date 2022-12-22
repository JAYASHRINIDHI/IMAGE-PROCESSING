#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
image=cv2.imread("download.jfif",0)

cv2.imshow('to display images',image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[2]:


cv2.imwrite("F:/jayashrinidhi/im1.png",image)


# In[3]:


#loading from external drive
image=cv2.imread("C:/Users/User/Downloads/images.jfif")
cv2.imshow('to display images',image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[17]:


#height and width
from PIL import Image

x="download (4).jfif"
img=Image.open(x)
width=img.width
height=img.height

print("The width of the image is",width)
print("The height of the image is",height)


# In[5]:


#no of channelsin color omage

import numpy
img=cv2.imread("download (5).jfif")
print("No of channels is:"+str(img.ndim))
print("No of channels is:",img.shape)
cv2.imshow("channel",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[6]:


#no of channels in greyscale omage

import numpy
img=cv2.imread("download (5).jfif",0)
print("No of channels is:"+str(img.ndim))
print("No of channels is:",img.shape)
ret,bw_img=cv2.threshold(img,127,225,cv2.THRESH_BINARY)


# In[7]:


#resize image
from PIL import Image
filepath="download (5).jfif"
im=Image.open(filepath)
new_im=im.resize((400,400))
new_im


# In[8]:


#matrix respresenation

import matplotlib.image as image
img=image.imread("images.jfif")
print("The shape of the image is",img.shape)
print("The array of the image is")
print(img)


# In[9]:


#binary image

import cv2
img=cv2.imread("images.jfif")
ret,bw_img=cv2.threshold(img,127,225,cv2.THRESH_BINARY)

#converting to its  binary form

bw=cv2.threshold(img,127,225,cv2.THRESH_BINARY)
cv2.imshow("BINARY",bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[10]:


import cv2
img=cv2.imread("images.jfif")
B,G,R=cv2.split(img)
print(B)
print(G)
print(R)


# In[11]:


img=cv2.imread("images.jfif")
cv2.imshow("original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[12]:


cv2.imshow("BLUE",B)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[13]:


cv2.imshow("GREEN",G)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[14]:


cv2.imshow("RED",R)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[15]:


#ASPECT RATIO
img=cv2.imread("images.jfif")
new_im=im.resize((400,200))
ar=1*(img.shape[1]/img.shape[0])
print("Aspect ratio")
print(ar)


# In[18]:


#mirror image
from PIL import Image, ImageOps
im = Image.open("download.jfif")
hori_filppedImage=im.transpose(Image.FLIP_LEFT_RIGHT)
hori_filppedImage.show()

vert_filppedImage=im.transpose(Image.FLIP_TOP_BOTTOM)
vert_filppedImage.show()


# In[ ]:


import cv2
img1=cv2.imread("nai.jfif")
img2=cv2.imread("bunny.jfif")
sum=img1+img2
sub=img1-img2
mul=img1*img2
div=img1/img2
cv2.imshow("sub",sub)
cv2.imshow("sum",sum)
cv2.imshow("mul",mul)
cv2.imshow("div",div)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




