#!/usr/bin/env python
# coding: utf-8

# In[25]:


#restoring a damaged image
import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage.restoration import inpaint
 
# Open the image.
img = plt.imread('cat_damaged.png')
plt.imshow(img)
plt.show()
 
# Load the mask.
mask = plt.imread('cat_mask.png',0)
plt.imshow(mask)
plt.show()
 
# Inpaint.
dst = inpaint.inpaint_biharmonic(img, mask, multichannel=True)

# Write the output.

plt.imshow(dst)
plt.show()


# In[16]:


#removing Logo's
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams["figure.figsize"]=(10,8)


# In[17]:


def show_image(image,title="image",cmap_type="gray"):
    plt.imshow(image,cmap=cmap_type)
    plt.title(title)
    plt.axis("off")


# In[18]:


def plot_comparison(img_original,img_filtered,img_title_filtered):
    fig,(ax1,ax2)=plt.subplots(ncols=2,figsize=(10,8),sharex=True,sharey=True)
    ax1.imshow(img_original,cmap=plt.cm.gray)
    ax1.set_title("original")
    #ax1.axis('off')
    ax2.imshow(img_filtered,cmap=plt.cm.gray)
    ax2.set_title(img_title_filtered)
    #ax2.axis('off')


# In[19]:


from skimage.restoration import inpaint
from skimage.transform import resize
from skimage import color


# In[21]:


image_with_logo=plt.imread("C:/Users/User/Downloads/logo.png")
mask=np.zeros(image_with_logo.shape[:-1])
mask[210:290,360:425]=1
image_logo_removed=inpaint.inpaint_biharmonic(image_with_logo,mask,multichannel=True)
plot_comparison(image_with_logo,image_logo_removed,"image with logo removed")


# In[ ]:




