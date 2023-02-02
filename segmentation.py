#!/usr/bin/env python
# coding: utf-8

# In[5]:


from skimage.segmentation import slic
from skimage.color import label2rgb
#adding noice 
import matplotlib.pyplot as plt

face_image=plt.imread("fface.jpg")

segments=slic(face_image,n_segments=400)

segmented_image=label2rgb(segments,face_image,kind="avg")

plt.title("original")
plt.imshow(face_image.astype('uint8'))
plt.show()

plt.title("denoisy image")
plt.imshow(segmented_image.astype('uint8'))
plt.show()


# In[ ]:




