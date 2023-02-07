#!/usr/bin/env python
# coding: utf-8

# In[23]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn")

loaded_image= cv2.imread("apple.jpg")
loaded_image=cv2.cvtColor(loaded_image,cv2.COLOR_BGR2RGB)

gray_image=cv2.cvtColor(loaded_image,cv2.COLOR_BGR2GRAY)

edged_image=cv2.Canny(gray_image,threshold1=280,threshold2=280)

plt.figure(figsize=(20,20))
plt.subplot(1,3,1)
plt.imshow(loaded_image,cmap="gray")
plt.title("original image")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(gray_image,cmap="gray")
plt.title("grayscale image")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(edged_image,cmap="gray")
plt.title("canny edge detected image")
plt.axis("off")


# In[27]:


#laplacian and sobel edge  detecting methods
import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("apple.jpg",)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

image=cv2.GaussianBlur(gray,(3,3),0)

laplacian=cv2.Laplacian(image,cv2.CV_64F)
sobelx=cv2.Sobel(image,cv2.CV_64F,1,0,ksize=5)
sobely=cv2.Sobel(image,cv2.CV_64F,0,1,ksize=5)

plt.subplot(2,2,1),plt.imshow(image,cmap="gray")
plt.title("original"),plt.xticks([]),plt.yticks([])

plt.subplot(2,2,2),plt.imshow(laplacian,cmap="gray")
plt.title("Laplacian"),plt.xticks([]),plt.yticks([])

plt.subplot(2,2,3),plt.imshow(sobelx,cmap="gray")
plt.title("sobel x"),plt.xticks([]),plt.yticks([])

plt.subplot(2,2,4),plt.imshow(sobely,cmap="gray")
plt.title("sobel y"),plt.xticks([]),plt.yticks([])

plt.show()


# In[31]:


#prewitt operator
import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("apple.jpg",)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

image=cv2.GaussianBlur(gray,(3,3),0)

kernelx=np.array([[1,1,0],[0,0,0],[-1,-1,-1]])
kernely=np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx=cv2.filter2D(image,-1,kernelx)
img_prewitty=cv2.filter2D(image,-1,kernely)

cv2.imshow("original Image",img)
cv2.imshow("prewitt x",img_prewittx)
cv2.imshow("prewitt y",img_prewitty)
cv2.imshow("prewitt",img_prewittx+img_prewitty)
cv2.waitKey()
cv2.destroyAllWindows()


# In[32]:


import cv2
import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt
roberts_cross_v = np.array( [[1, 0 ],[0,-1]])

roberts_cross_h =np.array( [[0, 1 ],[-1,0]])
img = cv2.imread("apple.jpg",0) .astype( 'float64')
img/=255.0

vertical = ndimage.convolve( img, roberts_cross_v )
horizontal = ndimage.convolve( img, roberts_cross_h )

edged_img =np.sqrt(np.square(horizontal) + np.square(vertical))
edged_img*=255
cv2.imwrite("output.jpg",edged_img)
cv2.imshow("OutputImage",edged_img)
cv2.waitKey()
cv2.destroyAllWindows()


# In[ ]:




