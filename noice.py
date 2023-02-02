#!/usr/bin/env python
# coding: utf-8

# In[17]:


#adding noice 
import matplotlib.pyplot as plt
from skimage.util import random_noise

image=plt.imread("cat_inpainted.png")
noice_img=random_noise(image)

plt.title("original")
plt.imshow(image)
plt.show()

plt.title("noisy image")
plt.imshow(noice_img)
plt.show()


# In[20]:


#reducing noise
from skimage.restoration import denoise_tv_chambolle
noisy_image=plt.imread("C:/Users/User/Downloads/nn.jpg")

denoised_image=denoise_tv_chambolle(noisy_image,multichannel=True)

plt.title("original")
plt.imshow(noisy_image)
plt.show()

plt.title("denoisy image")
plt.imshow(denoised_image)
plt.show()


# In[21]:


#reducing noise while preserving edges
from skimage.restoration import denoise_bilateral
noisy_image=plt.imread("C:/Users/User/Downloads/nn.jpg")

denoised_image=denoise_bilateral(noisy_image,multichannel=True)

plt.title("original")
plt.imshow(noisy_image)
plt.show()

plt.title("denoisy image")
plt.imshow(denoised_image)
plt.show()


# In[ ]:




