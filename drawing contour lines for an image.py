#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Drawing contour lines for an image.
import cv2
import numpy as np
  
image = cv2.imread('sss.png')
cv2.waitKey(0)
  
# Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
# Find Canny edges
edged = cv2.Canny(gray, 30, 200)
cv2.waitKey(0)
  
contours, hierarchy = cv2.findContours(edged, 
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
  
cv2.imshow('Canny Edges After Contouring', edged)
cv2.waitKey(0)
  
# Draw all contours

cv2.drawContours(image, contours, -1, (255, 0, 0), 3)
  
cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




