#!/usr/bin/env python
# coding: utf-8

# In[9]:


import cv2
img = cv2.imread("f8.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

faces = face_cascade.detectMultiScale(gray, 1.3, 4)
print('Number of detected faces:', len(faces))

# loop over the detected faces
for (x,y,w,h) in faces:
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
   
   # detects eyes of within the detected face area (roi)
    eyes = eye_cascade.detectMultiScale(roi_gray)
   
   # draw a rectangle around eyes
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,255),2)

# display the image with detected eyes
cv2.imshow('Eyes Detection',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




