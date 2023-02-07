#!/usr/bin/env python
# coding: utf-8

# In[1]:


#listing only png images
import os
from os import listdir
 
# get the path/directory
folder_dir = "C:/Users/User/Downloads"
for images in os.listdir(folder_dir):
 
    # check if the image ends with png
    if (images.endswith(".png")):
        print(images)


# In[2]:


#lisiting all the mages
import os
from os import listdir
 
# get the path/directory
folder_dir = "C:/Users/User/Downloads"
for images in os.listdir(folder_dir):
    print(images)


# In[1]:


import cv2 
import os 
import glob 
img_dir = "C:/Users/User/Downloads" # Enter Directory of all images  
data_path = os.path.join(img_dir,'*g') 
files = glob.glob(data_path) 
data = [] 
for f1 in files: 
    img = cv2.imread(f1) 
    data.append(img) 


# In[23]:


#displaying all the images from the folder
import cv2 
import os 
import glob 
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
 
#Set the path where images are stored 
img_dir = "C:/Users/User/Downloads" # Enter Directory of all images  
data_path = os.path.join(img_dir,'*g') 
files = glob.glob(data_path) 
data = [] 
for f1 in files: 
    img = plt.imread(f1,0) 
    data.append(img) 
    plt.figure() 
    plt.title("original Image")
    plt.imshow(img) 
for f1 in files: 
    img = plt.imread(f1,0) 
    data.append(img) 
    resize=cv2.resize(img,(100,100))
    plt.figure() 
    plt.title("resized Image")
    plt.imshow(resize)


# In[ ]:




