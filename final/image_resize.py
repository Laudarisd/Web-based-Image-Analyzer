# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 16:22:44 2019

@author: tatha
"""

import cv2
import os

path = "data/obj/fruits-360_dataset/fruits-360/Training"
tpath = "data/obj/fruits-360_dataset/fruits-360/Test"

def resize(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image,(416,416))
    return image

classlist = os.listdir(path)
for classes in classlist:
    images = os.listdir(path + "/" + classes)
    for image in images:
        if image.endswith(".jpg"):
            imn = image
            im = resize(path + "/" + classes + "/" + image)
            print(path + "/" + classes + "/" + image)
            os.remove(path + "/" + classes + "/" + image)
            fstr = path + "/" + classes + "/" + imn.split(".")[0] + '.jpg'
            print(fstr)
            cv2.imwrite(fstr,im)
            
            
            
            

classlist = os.listdir(tpath)
for classes in classlist:
    images = os.listdir(tpath + "/" + classes)
    for image in images:
        if image.endswith(".jpg"):
            imn = image
            im = resize(tpath + "/" + classes + "/" + image)
            os.remove(tpath + "/" + classes + "/" + image)
            fstr = tpath + "/" + classes + "/" + imn.split(".")[0] + '.jpg'
            cv2.imwrite(fstr,im)
            