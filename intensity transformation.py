#!/usr/bin/env python
# coding: utf-8

# In[1]:


#image neagative
get_ipython().run_line_magic('matplotlib', 'inline')
import imageio
import matplotlib.pyplot as plt
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)
pic=imageio.imread("b.png")
plt.figure(figsize=(6,6))
plt.imshow(pic)
plt.axis("off")


# In[2]:


negative=255-pic #neg=(L-1)-img
plt.figure(figsize=(6,6))
plt.imshow(negative);
plt.axis("off");


# In[3]:


#log transformation
get_ipython().run_line_magic('matplotlib', 'inline')
import imageio
import matplotlib.pyplot as plt
import numpy as np

pic=imageio.imread("b.png")
gray=lambda rgb : np.dot(rgb[...,:3],[0.299,0.587,0.114])
gray=gray(pic)

max_=np.max(gray)

def log_transform():
    return(255/np.log(1+max_))*np.log(1+gray)
plt.figure(figsize=(5,5))
plt.imshow(log_transform(),cmap=plt.get_cmap(name="gray"))
plt.axis("off");


# In[4]:


#gamma correction
import imageio
import matplotlib.pyplot as plt

#gamma encoding
pic=imageio.imread("b.png")
gamma=2.2 #gamma<1 ~ Dark:gamma>1~ bright

gamma_correction=((pic/255)**(1/gamma))
plt.figure(figsize=(5,5))
plt.imshow(gamma_correction)
plt.axis("off");

