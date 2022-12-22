#!/usr/bin/env python
# coding: utf-8

# In[1]:


#converting from one file format to another
from PIL import Image
image=Image.open("a.jfif")

image.save("b.png")
print("successfully converted")


# In[2]:


#from one mode to another
from PIL import Image
image=Image.open("a.jfif")
image=image.convert("1")
image.show()


# In[3]:


print(image.mode)


# In[12]:


#different color spaces
import cv2
img=cv2.imread("b.png")
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lab=cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
hls=cv2.cvtColor(img,cv2.COLOR_BGR2HLS)
yuv=cv2.cvtColor(img,cv2.COLOR_BGR2YUV)

cv2.imshow("GREY",grey)
cv2.imshow("HSV",hsv)
cv2.imshow("LAB",lab)
cv2.imshow("HLS",hls)
cv2.imshow("YUV",yuv)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[5]:


#cropping image
import cv2
image = cv2.imread("b.png")

cropped_img = image[50:200, 100:400]

cv2.imshow("Original image", image)
cv2.imshow("Cropped image", cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[6]:


#histogram
import matplotlib.pyplot as plt
im=Image.open("b.png")
pl=im.histogram()
plt.bar(range(256),pl[:256],color="r",alpha=0.5)
plt.bar(range(256),pl[256:2*256],color="g",alpha=0.4)
plt.bar(range(256),pl[2*256:],color="b",alpha=0.3)
plt.show()


# In[9]:


#negating an image
im = Image.open("b.png") 
im_t = im.point(lambda x: 255 - x)
im_t.show()


# In[10]:


#RGB channels
from skimage.io import imread,imshow
import matplotlib.pyplot as plt
img = imread("b.png")
imshow(img)

fig,ax=plt.subplots(1,3,figsize=(12,4),sharey=True)

ax[0].imshow(img[:,:,0],cmap='Reds')
ax[0].set_title("RED")
ax[1].imshow(img[:,:,1],cmap="Greens")
ax[1].set_title("GREEN")
ax[2].imshow(img[:,:,2],cmap="Blues")
ax[2].set_title("BLUE")


# In[35]:


#text on image
from PIL import Image,ImageDraw,ImageFont
img = Image.open("b.png")
draw = ImageDraw.Draw(img)
txt="hello world"

font = ImageFont.truetype('ALGER.TTF',20)

draw.text((20,20),txt,font=font)
img.show()


# In[15]:


#image blending
im1=Image.open("nai.jfif")
im2=Image.open("bunny.jfif")
alpha1=Image.blend(im1,im2,alpha=0.4)
alpha2=Image.blend(im1,im2,alpha=0.4)
alpha1.show()
alpha2.show()


# In[28]:


#statics
from PIL import Image,ImageStat
im=Image.open("bunny.jfif")
stat=ImageStat.Stat(im)
print("MEAN",stat.mean)
print("MEDIAN",stat.median)
print("mode",stat.stddev)


# In[3]:


#slicing
from skimage.io import imread,imshow
import matplotlib.pyplot as plt
img = imread("b.png")
imshow(img)

fig,ax=plt.subplots(1,3,figsize=(12,4),sharey=True)

ax[0].imshow(img[:,0:130])
ax[0].set_title("FIRST SPLIT")
ax[1].imshow(img[:,130:260])
ax[1].set_title("SECOND SPLIT")
ax[2].imshow(img[:,120:290])
ax[2].set_title("THIRD SPLIT")


# In[ ]:




