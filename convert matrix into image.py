#!/usr/bin/env python
# coding: utf-8

# In[2]:


from PIL import Image
import numpy as np
# Creating the 144 X 144 NumPy Array with random values
arr = np.random.randint(255, size=(244, 244), dtype=np.uint8)
# Converting the numpy array into image
img  = Image.fromarray(arr)
# Saving the image
img.save("Image_from_array.png")
print(" The Image is saved successfully")
img.show()


# In[ ]:





# In[ ]:




