#!/usr/bin/env python
# coding: utf-8

# In[17]:


#difference between 2 images

# import module
from PIL import Image, ImageChops
from matplotlib import pyplot as plt
  
# assign images
img1 = Image.open("1img.png")
plt.imshow(img1)
plt.show()
img2 = Image.open("2img.png")
plt.imshow(img2)
plt.show()
  
# finding difference
diff = ImageChops.difference(img1, img2)
plt.imshow(diff)
plt.show()


# In[ ]:




