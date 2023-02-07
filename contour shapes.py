#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Contouring shape
import matplotlib.pyplot as plt
def show_image_contour(image,contours):
    plt.figure()
    for n,contour in enumerate(contours):
        plt.plot(contour[:,1],contour[:,0],linewidth=3)
    plt.imshow(image,interpolation='nearest',cmap='gray_r')
    plt.title('Contours')
    plt.axis('off')


# In[3]:


from skimage import measure,data
horse_image=data.horse()
contours=measure.find_contours(horse_image,level=0.8)
show_image_contour(horse_image,contours)


# In[5]:


#Find the contours of an image that is not binary
from skimage.io import imread
from skimage import color
from skimage.filters import threshold_otsu
image_dices=imread('dice.jpg')
image_dices=color.rgb2gray(image_dices)
thresh=threshold_otsu(image_dices)
binary=image_dices>thresh
contours=measure.find_contours(binary,level=0.8)
show_image_contour(image_dices,contours)


# In[6]:


#Count the dots in a dice's image
import numpy as np
shape_contours=[cnt.shape[0] for cnt in contours]
max_dots_shape=200
dots_contours=[cnt for cnt in contours if np.shape(cnt)[0] < max_dots_shape]
show_image_contour(binary,contours)
print("Dice's dots number: {}.".format(len(dots_contours)))


# In[ ]:




