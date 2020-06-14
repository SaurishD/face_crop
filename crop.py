# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 10:26:58 2019

@author: Saurish
"""

import cv2
import os


out_path = 'output/'
in_path = 'input/'
#You can change your size here
out_size = (300,300)
i = 0
face_cascade = cv2.CascadeClassifier('hc_face.xml')

for file in os.listdir(in_path):
    if file.endswith('.jpg') or file.endswith('.jpeg'):
        print(file)
        img = cv2.imread(in_path+file,0)
        faces = face_cascade.detectMultiScale(img,1.3,5)
        for (x,y,w,h) in faces:
            temp_img = img[y:y+h,x:x+w]
            temp_img = cv2.resize(temp_img,out_size)
            cv2.imwrite(os.path.join(out_path , str(i)+'.jpg'), temp_img)
            i = i+1


