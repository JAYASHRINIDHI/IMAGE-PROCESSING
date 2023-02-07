#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image
import os

os.getcwd()


# In[2]:


image1 = Image.open("fface.jpg")

image1


# In[3]:


image1.show()


# In[4]:


image1.save("pic1.png")


# In[5]:


os.listdir()


# In[6]:


for f in os.listdir("."):
    if f.endswith(".jpg"):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        print(fn, "&", fext)


# In[7]:


for f in os.listdir("."):
    if f.endswith(".jpg"):
        print(f)


# In[8]:


os.mkdir('NewExtnsn')


# In[12]:


for f in os.listdir("."):
    if f.endswith(".png"):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        i.save("NewExtnsn/{}.pdf".format(fn))


# In[13]:


#resizing

os.makedirs('resize//small')
os.makedirs('resize//tiny')


# In[15]:


size_small = (600,600) # small images of 600 X 600 pixels
size_tiny = (200,200)  # tiny images of 200 X 200 pixels
for f in os.listdir("."):
    if f.endswith(".png"):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        i.thumbnail(size_small)
        i.save("resize/small/{}_small{}".format(fn, fext))
        i.thumbnail(size_tiny)
        i.save("resize/tiny/{}_tiny{}".format(fn, fext))


# In[19]:


#rotating

#rotating the image to 55 Degree angle
image3 = Image.open("cat.png")
image3.rotate(55).save("image3.jpg")
Image3 = Image.open("image3.jpg")
Image3


# In[22]:


# Creating new Directory using OS library
os.mkdir('rotate')
for f in os.listdir("."):
    if f.endswith(".png"):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        im = i.rotate(90)
        im.save("rotate/{}_rot.{}".format(fn, fext))


# In[ ]:




