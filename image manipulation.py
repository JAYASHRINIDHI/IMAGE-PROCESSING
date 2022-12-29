#!/usr/bin/env python
# coding: utf-8

# In[1]:


#image sharpen
from PIL import Image
from PIL import ImageFilter
import matplotlib.pyplot as plt
 
my_image=Image.open("b.png") 

sharp=my_image.filter(ImageFilter.SHARPEN)

sharp.save("E:\jayashrinidhi\sharpen.jpg")
sharp.show()
plt.imshow(sharp)
plt.show()


# In[2]:


#image flip
import matplotlib.pyplot as plt
img=Image.open("letter.jpg") 
plt.imshow(img)
plt.show()

flip=img.transpose(Image.FLIP_LEFT_RIGHT)
flip.save("E:/jayashrinidhi/flip.png")
plt.imshow(flip)
plt.show()


# In[1]:


#cropping
from PIL import Image
import matplotlib.pyplot as plt

im=Image.open("b.png")
width,height=im.size
im1=im.crop((55,30,200,160))

im1.show()
plt.imshow(im1)
plt.show()

