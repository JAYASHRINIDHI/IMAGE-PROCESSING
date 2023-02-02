#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image
from PIL import ImageFilter
import os

def main():
# path of the folder containing the raw images
    inPath ="F:/Jayashrinidhi"

# path of the folder that will contain the modified image
    outPath ="F:/new"
    
    for imagePath in os.listdir(inPath):
# imagePath contains name of the image
        inputPath = os.path.join(inPath, imagePath)

# inputPath contains the full directory name
        img = Image.open(inputPath)

        fullOutPath = os.path.join(outPath, 'invert_'+imagePath)
# fullOutPath contains the path of the output
# image that needs to be generated
        img.rotate(90).save(fullOutPath)

        print(fullOutPath)

# Driver Function
if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:




